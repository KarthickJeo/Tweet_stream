from flask import Flask,request
app = Flask(__name__)
# Create the appropriate app.route functions, test and see if they work, and paste your URI’s in the boxes below.
def getAllPuppies():
  return "Getting All the puppies!"

def makeANewPuppy():
  return "Creating A New Puppy!"

def getPuppy(id):
	return "Getting Puppy with id %s" %id

def updatePuppy(id):
  return "Updating a Puppy with id %s" % id

def deletePuppy(id):
  return "Removing Puppy with id %s" % id
#Make an app.route() decorator here
@app.route('/puppiesFunction',methods=['GET','POST'])
def puppiesFunction():
  if request.method == 'GET':
      return (getAllPuppies())

  	#Call the method to Get all of the puppies


  elif request.method == 'POST':
      return (makeANewPuppy())
  	#Call the method to make a new puppy



#Make another app.route() decorator here that takes in an integer id in the
@app.route('/puppiesFunctionId/<id>', methods=['GET','PUT','DELETE'])
def puppiesFunctionId(id):
  if request.method == 'GET':
      return (getPuppy(id))
  	#Call the method to get a specific puppy based on their id

  if request.method == 'PUT':
      return (updatePuppy(id))
  	#Call the method to update a puppy

  elif request.method == 'DELETE':
      return (deletePuppy(id))
  	#Call the method to remove a puppy


if (__name__) == ('__main__'):
    app.run(debug=True)