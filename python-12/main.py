
doc = '''
#%RAML 1.0
title: clientes-api
version: v1
mediaType: application/json

securitySchemes:
  JWT:
    description: JWT Auth
    type: x-{other}
    describedBy:
      headers:
        Authorization:
          description: X-AuthToken
          type: string
          required: true
      responses:
        201:
          body:
            application/json:
              description: Token has been generated
        400:
          body:
            application/json:
              description: Token has expired
    settings:
        roles: []
types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
  Agent:
    type: object
    discriminator: agent
    properties:
      agent_id:
        type: integer
        required: true
        example: 2
      name:
        type: string
        required: true
        example: "jesus"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "opa"
      version:
        type: string
        required: true
        example: "2"
      address:
        type: string
        required: true
        example: "192.168.0.1"
    example:
        agent_id: 2
        user_id: 3
        name: "agent name"
        status: true
        environment: "env"
        version: "1"
        address: "1.1.1.1"
  Event:
    discriminator: event
    type: object
    properties:
      event_id:
        type: integer
        required: true
        example: 2
      level:
        type: string
        required: true
        example: "opa"
      payload:
        type: string
        required: true
        example: "opa"
      shelved:
        type: boolean
        required: true
        example: true
      address:
        type: string
        required: true
        example: "192.168.0.1"
      date:
          type: string
          format: date-time
          required: true
          example: "2020-01-11"
      agent_id:
        type: integer
        required: true
        example: 2
    example:
        event_id: 2
        agent_id: 3
        level: "level"
        payload: "teste"
        shelve: true
        data: "2020-01-11"
    Response:
        discriminator: response
        properties:
            message:
                type: string
                example: "res"
  Group:
    discriminator: group
    type: object
    properties:
      group_id:
        type: integer
        required: true
        example: 2
      name:
        type: string
        required: true
        example: "teste"
    example:
        group_id: 1
        name: "name"
  User:
    discriminator: user
    type: object
    properties:
      user_id:
        type: integer
        required: true
        example: 2
      name:
        type: string
        required: true
        example: "teste"
      password:
        type: string
        required: true
        example: "teste"
      email:
        type: string
        required: true
        example: "teste"
      last_login:
          type: string
          format: date
          required: true
          example: "2020-11-20"
      group_id:
          type: integer
          required: true
          example: 2
    example:
        user_id: 1
        name: "name"
        email: "email@email"
        last_login: "2020-01-11"
        group_id: 1
/auth/token:
  get:
    description: get token
    responses:
      200:
        body:
          type: Response
        example: token da massa
      401:
        body:
          type: Response
        example: Unauthorized
      404:
        body:
          type: Response
        example: Unauthorized
  post:
    description: none
    securedBy: [JWT]
    body:
        application/json:
          type: string
          username: string
          password: string
    responses:
      201:
        body:
          application/json:
              description: Valid Token
      400:
        body:
          application/json:
              description: teste
/agents:
  get:
    description: None
    securedBy: [JWT]
    responses:
      200:
        body:
          type: Agent[]
        example:
            message: teste
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  post:
    description: none
    securedBy: [JWT]
    body:
      application/json:
        properties:
        example: teste
    responses:
      201:
        body:
          type: Response
        example:
          mensagem: Created
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  /{id}:
    get:
      securedBy: [JWT]
      description: Agent detail
      responses:
        200:
          body:
            type: Agent
          example:
            mensagem: Agent
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    put:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Agent
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    delete:
      description: Teste
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
          example:
            mensagem: deleted
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/events:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event[]
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    post:
      description: none
      securedBy: [JWT]
      body:
        application/json:
            properties:
            example: {}
        201:
          body:
            type: Response
          example:
            mensagem: Created
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    put:
      securedBy: [JWT]
      description: None
      body:
          application/json:
              properties:
              example: {}
          200:
            body:
              type: Response
            example:
              mensagem: Created
          401:
            body:
              type: Mensagem
            example:
              mensagem: unauthorized
          404:
            body:
              type: Mensagem
            example:
              mensagem: Not found
    delete:
      description: none
      securedBy: [JWT]
      body:
        application/json:
            properties:
            example: {}
        example:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
  /{id}/events/{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
/groups:
  get:
    description: None
    securedBy: [JWT]
    responses:
      200:
        body:
          type: Group[]
        example:
          mensagem: teste
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  post:
    description: none
    securedBy: [JWT]
    body:
      application/json:
        properties:
          name: string
        example: {
                   name: "teste"
        }
    responses:
      201:
        body:
          type: Response
        example:
          mensagem: Created
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  /{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Group
          example:
            mensagem: Created
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    put:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Group
          example:
            mensagem: Created
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    delete:
      description: None
      securedBy: [JWT]
      responses:
        204:
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
/users:
  get:
    description: None
    securedBy: [JWT]
    responses:
      200:
        body:
          type: User[]
        example:
          mensagem: Created
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  post:
    description: Create User
    securedBy: [JWT]
    body:
        application/json:
            properties:
                example: {}
    responses:
      201:
        body:
          type: Response
        example:
          mensagem: Created
      401:
        body:
          type: Response
        example:
          mensagem: Unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  /{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Response
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    put:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Response
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    delete:
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Response
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/agents:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Agent[]
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/agents/{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Agent
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/agents/{id}/events:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event[]
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/agents/{id}/events/{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event
          example:
            mensagem: teste
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
/events:
  get:
    description: None
    securedBy: [JWT]
    responses:
      200:
        body:
          type: Event[]
        example:
          mensagem: teste
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  post:
    description: none
    securedBy: [JWT]
    body:
        application/json:
            properties:
                example: {}
    responses:
      201:
        body:
          application/json:
            example: {
              "name": "name",
              "status": true,
              "environment": "environment",
              "version": "1",
              "address": "address"
            }
      401:
        body:
          type: Mensagem
        example:
          mensagem: unauthorized
      404:
        body:
          type: Mensagem
        example:
          mensagem: Not found
  /{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    put:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
    delete:
      securedBy: [JWT]
      responses:
        204:
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
  /{id}/agents/{id}:
    get:
      description: None
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Event
        401:
          body:
            type: Mensagem
          example:
            mensagem: unauthorized
        404:
          body:
            type: Mensagem
          example:
            mensagem: Not found
'''
