

CREATE TABLE "Computation" (
	context TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type TEXT NOT NULL, 
	keywords TEXT, 
	"runBy" TEXT NOT NULL, 
	"dateCreated" DATE NOT NULL, 
	description TEXT NOT NULL, 
	"associatedPublication" TEXT, 
	"calledBy" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Dataset" (
	context TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type TEXT NOT NULL, 
	keywords TEXT, 
	author TEXT NOT NULL, 
	"datePublished" DATE NOT NULL, 
	version TEXT NOT NULL, 
	description TEXT NOT NULL, 
	"associatedPublication" TEXT, 
	format TEXT NOT NULL, 
	"dataSchema" TEXT, 
	"contentUrl" TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Software" (
	context TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	type TEXT NOT NULL, 
	keywords TEXT, 
	author TEXT NOT NULL, 
	"dateModified" DATE NOT NULL, 
	version TEXT NOT NULL, 
	description TEXT NOT NULL, 
	"associatedPublication" TEXT, 
	format TEXT NOT NULL, 
	"contentUrl" TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Computation_additionalDocumentation" (
	backref_id TEXT, 
	"additionalDocumentation" TEXT, 
	PRIMARY KEY (backref_id, "additionalDocumentation"), 
	FOREIGN KEY(backref_id) REFERENCES "Computation" (id)
);

CREATE TABLE "Computation_usedSoftware" (
	backref_id TEXT, 
	"usedSoftware" TEXT NOT NULL, 
	PRIMARY KEY (backref_id, "usedSoftware"), 
	FOREIGN KEY(backref_id) REFERENCES "Computation" (id)
);

CREATE TABLE "Computation_usedDataset" (
	backref_id TEXT, 
	"usedDataset" TEXT, 
	PRIMARY KEY (backref_id, "usedDataset"), 
	FOREIGN KEY(backref_id) REFERENCES "Computation" (id)
);

CREATE TABLE "Computation_generated" (
	backref_id TEXT, 
	generated TEXT, 
	PRIMARY KEY (backref_id, generated), 
	FOREIGN KEY(backref_id) REFERENCES "Computation" (id)
);

CREATE TABLE "Dataset_additionalDocumentation" (
	backref_id TEXT, 
	"additionalDocumentation" TEXT, 
	PRIMARY KEY (backref_id, "additionalDocumentation"), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Dataset_generatedBy" (
	backref_id TEXT, 
	"generatedBy" TEXT, 
	PRIMARY KEY (backref_id, "generatedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Dataset_derivedFrom" (
	backref_id TEXT, 
	"derivedFrom" TEXT, 
	PRIMARY KEY (backref_id, "derivedFrom"), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Dataset_usedBy" (
	backref_id TEXT, 
	"usedBy" TEXT, 
	PRIMARY KEY (backref_id, "usedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Software_additionalDocumentation" (
	backref_id TEXT, 
	"additionalDocumentation" TEXT, 
	PRIMARY KEY (backref_id, "additionalDocumentation"), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_usedByComputation" (
	backref_id TEXT, 
	"usedByComputation" TEXT, 
	PRIMARY KEY (backref_id, "usedByComputation"), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);
