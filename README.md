# Ceres 

Ceres is the goddess of the agriculture. Take a seed and just call Ceres 
to make it grow the plant. After that, you just have to crop the result :)

It is the same idea that drive this tool : let the computer work for you !
Seriously, the Ceres tool is a code generator based on model/template. 
No UML, no complex stuff.

**Keep It Simple**

In one hand, there are collections of *entities* (YAML files) that create *models*.
In other hand, there are collections of *templates*. At least, both are stored in a
directory - the generation root - which contains a YAML file describing how to 
generate the code. 

```
.
+-- example
|   +-- model
|   |   +-- entity1.yml
|   |   +-- entity2.yml
|   |   +-- ...
|   +-- template
|   |   +-- code.yml
|   |   +-- test.yml
|   |   +-- ...
|   +-- build.yml
```

**Easy !**

The generation is straight forward :

```console
foo@bar:~$ python3 -m ceres example/ 
```

Now let's look how create your first project.

## Installation

From github :

```console
foo@bar:~$ git clone https://github.com/laulin/ceres
foo@bar:~$ cd ceres
foo@bar:~/ceres$ sudo make install
```

Obvioulsy you will need pip3 installed.

## Example

A good example is always better than documentation. So let me 
explain how to create your code generation.

***All files hereby can be found in *example/* directory.**

As explain in introduction, there are 3 types of files : entity file,
template file and build file.

### Entity file

It contains information for the code generation. The only
requirement it about the field *name* that must exist. An example 
can be this one :

```yaml
name: get_user
entity:
  username: 
    type: str
  password: 
    type: str

variables:
  on_success: 200
  on_fail: 404
  action: GET

tests:
  on_success:
    username: foo
    password: bar
  on_fail:
    username: a
    password: b
```

The are section here :

- entity : contain the data model
- variables : contains variable needed in addition to entity to 
    generate the code
- tests : contains test vectors

You can imagine to add your own section, it's up to you !

#### Aggregate

**Advanced topic, you can skip it at first time**

In some case, you may need to send many models *at same time* to a temple. 
You can see this in the *router* case of the example. 

To do that you have to add a key *aggregate: true* in the target. All 
models will be merge in a dict called *models*, directly available in 
the template. 

### Template file

Like the name suggest, it contains the code template. The template engine is 
Mako. You can find the documentation here :

- https://docs.makotemplates.org/en/latest/

```mako
def ${variables["action"]}_${name}(\
%for k, v in entity.items():
${k}:${v["type"]}${'):' if loop.last else ', '}\
%endfor

    tmp = \
%for k, v in entity.items():
str(${k})${'' if loop.last else ' + '}\
%endfor

    if len(tmp) < 5:
        return ${variables["on_fail"]}
    else:
        return ${variables["on_success"]}
```

Basically, the entity yaml file is load and forwarded as dict to the template
engine. So you can retrive all keys and values during the render. 

### Build file

Well, at this point the explanation is coming to an end. To orchestrate all the 
generation, a yaml file is present at the root directory. Each target - define 
as a key in dict - must contains thee following keys :

- model : define the path of entity(ies). Unix style path, can use pattern (?, *, [], ...)
- template : define the path of templates. Unix style path, can use pattern (?, *, [], ...)
- output : define the path and the name of the output file. Can use so tag like :
    * {pwd} : working dir of the generation
    * {entity_name} : the *name* field in entity
    * {template_name} : the *name* field in entity

Let's look at the file in *example/*: 

```yaml
request code:
  model: model/*.yml
  template: template/request.py.mako
  output: "{pwd}/{template_name}_{entity_name}.py"

request test:
  model: model/*.yml
  template: template/test_request.py.mako
  output: "{pwd}/{template_name}_{entity_name}.py"
```
There is two target : *request code* and *request test*. Both use the pattern
N to 1 (multi entity, single model). You also do the opposite (1 to N) or 
a simple 1 to 1. 

# Thanks

- Laurent GUERIN for his tools Telosys (https://www.telosys.org/). I was 
  inspired by this tool to make Ceres.
- Yohann - "Yohann who ?" - to introduce Telosys :)
