"""
Django settings for the poker project.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from web3.auto import w3

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zarim86b1h6+8-svv=jh6g7&@)6(&6w(s#isma$usp70&f013l'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Ethereum Mainet
#ETHEREUM_CHAINID = 1
#ETHEREUM_PROVIDER_HOST = "mainnet.infura.io"
#ETHEREUM_PROVIDER = "https://"+ETHEREUM_PROVIDER_HOST+"/v3/48b4ad627f2045c9a4ccb21e50d3cca5"
#ETHEREUM_WEBSOCKET_PROVIDER = "wss://"+ETHEREUM_PROVIDER_HOST+"/ws"
#ETHEREUM_MASTER_WALLET = ""

# Ethereum Testnet
ETHEREUM_CHAINID = 3
ETHEREUM_PROVIDER_HOST = "ropsten.infura.io"
ETHEREUM_PROVIDER = "https://"+ETHEREUM_PROVIDER_HOST+"/xSKHv68S1At0vV7kPPXL"
ETHEREUM_WEBSOCKET_PROVIDER = "wss://"+ETHEREUM_PROVIDER_HOST+"/ws"
ETHEREUM_TEST_WALLET = "keystore/robot-test-wallet.json"

# Transactions throughput (1 cheapest, 1000 fastest)
ETHEREUM_GAS_PRICE = w3.toWei(3, 'gwei')
ETHEREUM_GAS_LIMIT = 1000000

# Ethereum smart-contract
ETHEREUM_CONTRACT_ADDRESS = '0xdf03c232474eb797f50b2c79b4e9c01a6c517454'
ETHEREUM_CONTRACT_ADDRESS = w3.toChecksumAddress(ETHEREUM_CONTRACT_ADDRESS)


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'game',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'game.urls'

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]

WSGI_APPLICATION = 'game.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


ETHEREUM_CONTRACT_ABI = """
[
	{
		"constant": false,
		"inputs": [],
		"name": "payRoyalty",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_player",
				"type": "address"
			},
			{
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "cashOut",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_paymentId",
				"type": "bytes32"
			}
		],
		"name": "verifyPayment",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getContractBalance",
		"outputs": [
			{
				"name": "balance",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_paymentId",
				"type": "bytes32"
			}
		],
		"name": "buyCredit",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "payOut",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_contract",
				"type": "address"
			}
		],
		"name": "GameStarted",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_player",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "PaymentReceived",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_player",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "PaymentMade",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_bandit",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "UnauthorizedCashoutAttempt",
		"type": "event"
	}
]
"""

ETHEREUM_CONTRACT_BYTECODE = """
{
	"linkReferences": {},
	"object": "608060405234801561001057600080fd5b507f67cf7f1535e1c1323fe4e76266f7d55f0c1f67fdf449db65e014f9d35881514d30604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a16106da806100836000396000f3fe6080604052600436106100555760003560e01c8063212d67231461005a578063224054431461007c57806348e68950146100e25780636f9fb98a14610135578063818a8abe14610160578063c2052403146101a6575b600080fd5b6100626101c8565b604051808215151515815260200191505060405180910390f35b6100c86004803603604081101561009257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506103af565b604051808215151515815260200191505060405180910390f35b3480156100ee57600080fd5b5061011b6004803603602081101561010557600080fd5b810190808035906020019092919050505061056a565b604051808215151515815260200191505060405180910390f35b34801561014157600080fd5b5061014a610593565b6040518082815260200191505060405180910390f35b61018c6004803603602081101561017657600080fd5b81019080803590602001909291905050506105b2565b604051808215151515815260200191505060405180910390f35b6101ae61065e565b604051808215151515815260200191505060405180910390f35b60008060023073ffffffffffffffffffffffffffffffffffffffff1631816101ec57fe5b049050600073cdad2d448583c1d9084f54c0d207b3ebe03984909050600073cdad2d448583c1d9084f54c0d207b3ebe03984909050600073d228c136b2234da6aea618bad77aceb618472af19050600073db45f16b2b7662601a9f56ee670bb5deb2efefae90508373ffffffffffffffffffffffffffffffffffffffff166108fc6064601e88028161027a57fe5b049081150290604051600060405180830381858888f193505050501580156102a6573d6000803e3d6000fd5b508273ffffffffffffffffffffffffffffffffffffffff166108fc6064601e8802816102ce57fe5b049081150290604051600060405180830381858888f193505050501580156102fa573d6000803e3d6000fd5b508173ffffffffffffffffffffffffffffffffffffffff166108fc6064601e88028161032257fe5b049081150290604051600060405180830381858888f1935050505015801561034e573d6000803e3d6000fd5b508073ffffffffffffffffffffffffffffffffffffffff166108fc6064600a88028161037657fe5b049081150290604051600060405180830381858888f193505050501580156103a2573d6000803e3d6000fd5b5060019550505050505090565b600080339050600073b3b8d45a26d16adb41278aa8685538b937487b1590508073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614610477577f42b91e62d1e0029f65ba9a6ea360260044361b9c7c1091fdecaacad5319e52918285604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060405180910390a1600092505050610564565b8473ffffffffffffffffffffffffffffffffffffffff166108fc859081150290604051600060405180830381858888f193505050501580156104bd573d6000803e3d6000fd5b507f0a58819e8a8484b4b953261f35757d54a8bb44412938c22784e056a69ffa17c9858386604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001828152602001935050505060405180910390a16001925050505b92915050565b600080600083815260200190815260200160002060009054906101000a900460ff169050919050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000803390506000349050600160008086815260200190815260200160002060006101000a81548160ff0219169083151502179055507f6ef95f06320e7a25a04a175ca677b7052bdd97131872c2192525a629f51be7708282604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060405180910390a1600192505050919050565b60003373ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f193505050501580156106a6573d6000803e3d6000fd5b50600190509056fea165627a7a72305820abfd6d8a034146099114c90f47e042bd6792fa9de8d5bdc32aada1faedb3bbff0029",
	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH32 0x67CF7F1535E1C1323FE4E76266F7D55F0C1F67FDF449DB65E014F9D35881514D ADDRESS PUSH1 0x40 MLOAD DUP1 DUP3 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 LOG1 PUSH2 0x6DA DUP1 PUSH2 0x83 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x55 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x212D6723 EQ PUSH2 0x5A JUMPI DUP1 PUSH4 0x22405443 EQ PUSH2 0x7C JUMPI DUP1 PUSH4 0x48E68950 EQ PUSH2 0xE2 JUMPI DUP1 PUSH4 0x6F9FB98A EQ PUSH2 0x135 JUMPI DUP1 PUSH4 0x818A8ABE EQ PUSH2 0x160 JUMPI DUP1 PUSH4 0xC2052403 EQ PUSH2 0x1A6 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x62 PUSH2 0x1C8 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 ISZERO ISZERO ISZERO ISZERO DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0xC8 PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x40 DUP2 LT ISZERO PUSH2 0x92 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x3AF JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 ISZERO ISZERO ISZERO ISZERO DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0xEE JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x11B PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x20 DUP2 LT ISZERO PUSH2 0x105 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x56A JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 ISZERO ISZERO ISZERO ISZERO DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x141 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x14A PUSH2 0x593 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x18C PUSH1 0x4 DUP1 CALLDATASIZE SUB PUSH1 0x20 DUP2 LT ISZERO PUSH2 0x176 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 ADD SWAP1 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP3 SWAP2 SWAP1 POP POP POP PUSH2 0x5B2 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 ISZERO ISZERO ISZERO ISZERO DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0x1AE PUSH2 0x65E JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP3 ISZERO ISZERO ISZERO ISZERO DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH1 0x0 DUP1 PUSH1 0x2 ADDRESS PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND BALANCE DUP2 PUSH2 0x1EC JUMPI INVALID JUMPDEST DIV SWAP1 POP PUSH1 0x0 PUSH20 0xCDAD2D448583C1D9084F54C0D207B3EBE0398490 SWAP1 POP PUSH1 0x0 PUSH20 0xCDAD2D448583C1D9084F54C0D207B3EBE0398490 SWAP1 POP PUSH1 0x0 PUSH20 0xD228C136B2234DA6AEA618BAD77ACEB618472AF1 SWAP1 POP PUSH1 0x0 PUSH20 0xDB45F16B2B7662601A9F56EE670BB5DEB2EFEFAE SWAP1 POP DUP4 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC PUSH1 0x64 PUSH1 0x1E DUP9 MUL DUP2 PUSH2 0x27A JUMPI INVALID JUMPDEST DIV SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x2A6 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP DUP3 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC PUSH1 0x64 PUSH1 0x1E DUP9 MUL DUP2 PUSH2 0x2CE JUMPI INVALID JUMPDEST DIV SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x2FA JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP DUP2 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC PUSH1 0x64 PUSH1 0x1E DUP9 MUL DUP2 PUSH2 0x322 JUMPI INVALID JUMPDEST DIV SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x34E JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP DUP1 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC PUSH1 0x64 PUSH1 0xA DUP9 MUL DUP2 PUSH2 0x376 JUMPI INVALID JUMPDEST DIV SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x3A2 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP PUSH1 0x1 SWAP6 POP POP POP POP POP POP SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP1 CALLER SWAP1 POP PUSH1 0x0 PUSH20 0xB3B8D45A26D16ADB41278AA8685538B937487B15 SWAP1 POP DUP1 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP3 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND EQ PUSH2 0x477 JUMPI PUSH32 0x42B91E62D1E0029F65BA9A6EA360260044361B9C7C1091FDECAACAD5319E5291 DUP3 DUP6 PUSH1 0x40 MLOAD DUP1 DUP4 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP3 POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 LOG1 PUSH1 0x0 SWAP3 POP POP POP PUSH2 0x564 JUMP JUMPDEST DUP5 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC DUP6 SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x4BD JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP PUSH32 0xA58819E8A8484B4B953261F35757D54A8BB44412938C22784E056A69FFA17C9 DUP6 DUP4 DUP7 PUSH1 0x40 MLOAD DUP1 DUP5 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP2 MSTORE PUSH1 0x20 ADD DUP4 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP4 POP POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 LOG1 PUSH1 0x1 SWAP3 POP POP POP JUMPDEST SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 DUP1 PUSH1 0x0 DUP4 DUP2 MSTORE PUSH1 0x20 ADD SWAP1 DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x0 KECCAK256 PUSH1 0x0 SWAP1 SLOAD SWAP1 PUSH2 0x100 EXP SWAP1 DIV PUSH1 0xFF AND SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 ADDRESS PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND BALANCE SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP1 CALLER SWAP1 POP PUSH1 0x0 CALLVALUE SWAP1 POP PUSH1 0x1 PUSH1 0x0 DUP1 DUP7 DUP2 MSTORE PUSH1 0x20 ADD SWAP1 DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x0 KECCAK256 PUSH1 0x0 PUSH2 0x100 EXP DUP2 SLOAD DUP2 PUSH1 0xFF MUL NOT AND SWAP1 DUP4 ISZERO ISZERO MUL OR SWAP1 SSTORE POP PUSH32 0x6EF95F06320E7A25A04A175CA677B7052BDD97131872C2192525A629F51BE770 DUP3 DUP3 PUSH1 0x40 MLOAD DUP1 DUP4 PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP2 MSTORE PUSH1 0x20 ADD SWAP3 POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 LOG1 PUSH1 0x1 SWAP3 POP POP POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 CALLER PUSH20 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF AND PUSH2 0x8FC CALLVALUE SWAP1 DUP2 ISZERO MUL SWAP1 PUSH1 0x40 MLOAD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP9 CALL SWAP4 POP POP POP POP ISZERO DUP1 ISZERO PUSH2 0x6A6 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP PUSH1 0x1 SWAP1 POP SWAP1 JUMP INVALID LOG1 PUSH6 0x627A7A723058 KECCAK256 0xab REVERT PUSH14 0x8A034146099114C90F47E042BD67 SWAP3 STATICCALL SWAP14 0xe8 0xd5 0xbd 0xc3 0x2a 0xad LOG1 STATICCALL 0xed 0xb3 0xbb SELFDESTRUCT STOP 0x29 ",
	"sourceMap": "25:2405:0:-;;;347:81;8:9:-1;5:2;;;30:1;27;20:12;5:2;347:81:0;395:26;415:4;395:26;;;;;;;;;;;;;;;;;;;;;;25:2405;;;;;;"
}
"""
