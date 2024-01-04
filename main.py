from fastapi import FastAPI, HTTPException, Request
from transformers import pipeline
from fastapi.templating import Jinja2Templates

# instancier l'application 
app_remi = FastAPI()

# charger le template de mise en page
templates = Jinja2Templates(directory="templates")

@app_remi.get("/")
async def read_item(request: Request):      # , id: str
    return templates.TemplateResponse(
    request=request, name="acceuil.html", context={"id": id}
)


# charge le modèle entrainé
reponse_pipeline = pipeline("models/model1")

# décorateur pour associer notre fonction "trouver_reponse" à la méthode HTTP GET
@app_remi.get("/generer_reponse")
def generer_reponse(question: str):

    # Utilise le modèle pour produire la réponse
    try:
        answer = reponse_pipeline(question=question)
	# Renvoyer la réponse obtenu avec le modèle au format JSON
        return {"question": question, "reponse": answer["answer"]}

    # Affiche erreur si problème (code 500 pour "catch-all")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# lance l'app
if __name__ == "__main__":
    import uvicorn

    # Démarre l'app sur un serveur local
    uvicorn.run(app_remi, host="127.0.0.1", port=8000)




# Dans le terminal, lancer l'app avec:
# $ uvicorn main:app --reload


# Dans les requirements, installer toutes les dependences et features
# $ pip install "fastapi[all]"
