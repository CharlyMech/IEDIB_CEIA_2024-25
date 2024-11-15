(define (domain transport)
    (:predicates (aeroport ?r)  (at ?c ?r)  (avio ?a)  (carrega ?c)  (dins ?c ?a))
    (:action carregar
        :parameters (?a ?c ?r)
        :precondition (and (at ?c ?r) (at ?a ?r) (carrega ?c) (avio ?a) (aeroport ?r))
        :effect (and (not (at ?c ?r)) (dins ?c ?a))
    )
     (:action descarregar
        :parameters (?a ?c ?r)
        :precondition (and (dins ?c ?a) (at ?a ?r) (carrega ?c) (avio ?a) (aeroport ?r))
        :effect (and (at ?c ?r) (not (dins ?c ?a)))
    )
     (:action volar
        :parameters (?a ?origen ?desti)
        :precondition (and (at ?a ?origen) (avio ?a) (aeroport ?origen) (aeroport ?desti))
        :effect (and (not (at ?a ?origen)) (at ?a ?desti))
    )
)