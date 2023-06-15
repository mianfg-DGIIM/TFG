[⬅ Más asignaturas del DGIIM](https://github.com/mianfg-DGIIM)

![Repo image](https://repository-images.githubusercontent.com/639075801/a17da198-d8b7-4a07-bbd0-2d700b867dff)

# `TFG` Trabajo de Fin de Grado (Bachelor's Thesis)

| Nombre                | Trabajo de Fin de Grado                                      |
| --------------------- | ------------------------------------------------------------ |
| Abreviatura           | `TFG`                                                        |
| Facultades            | Facultad de Ciencias<br/>Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación (ETSIIT)  |
| Universidad           | Universidad de Granada                                       |
| Tutor                 | Serafín Moral Callejón                                       |
| Departamento          | Ciencias de la Computación e Inteligencia Artificial         |
| Curso                 | 2022/2023                                                    |

## Información

> ⚠️ Este TFG se encuentra actualmente **en desarrollo**.

Este es el repositorio de mi **Trabajo de Fin de Grado** titulado ***"Una perspectiva algorítmica a la incompletitud de las Matemáticas"***.

## Contenidos

| Carpeta | Descripción |
| --- | --- |
| [`codigo`](./codigo) | Todo el código del trabajo |
| [`memoria`](./memoria) | Memoria del trabajo |

## Abstract

We begin this Bachelor’s Thesis highlighting the motivation behind this work, as well as the main goals to be achieved. Immediately after, we give a brief historical contextualization of the topics covered in this writing.

The theoretical development starts introducing a specific subset of Python programs, namely **SISO programs**, and we observe this class is as expressive as the class of all Python programs. Next, we delve into **Turing machines**, the main mathematical tool of our analysis. Afterwards, we introduce new and equivalent computing models, until we arrive at the main result of this chapter: the fact that Turing machines can emulate Python programs, and vice versa; in other words, Python programs and Turing machines are equivalent. This will allow us to use Python programs conveniently, instead of having to specify precise descriptions of Turing machines. We conclude the chapter introducing the **Church-Turing thesis**, and realizing that the equivalence result proved can be an argument in its favor.

We define mathematically the notion of **computational problem**, and we discuss Python programs (and, equivalently, Turing machines), can solve them. We call **decidable** any problem that can be solved by a program that never halts. We then observe a Python program can emulate itself, which leads us to the existence of **undecidable** problems. Following this, we relax the halting condition to obtain **semidecidable** problems. Afterwards, we introduce the **reduction** technique, which allows us to obtain new, undecidable problems, including the most important one for this thesis: the **halting problem**.

In order to prove the main result of this work, it is necessary to introduce a formalization of the concepts of **proof** and **truth**. This is precisely what we do when introducing **formal systems** and **logical systems**. Formal systems are **syntactic**: they formalize what a **theorem** is, a provable **formula** from a set of **axioms** and **inference rules**. On the other hand, logical systems incorporate to formal systems a semantic component: **truth**. We present essential properties of the aforementioned systems, which relate semantic and syntactic concepts. Afterwards we highlight the introduction of **Peano arithmetic**, a logical system of especial significance.

As colophon, we proceed to prove the **First Incompleteness Theorem**: we do so first from Peano arithmetic, and then we generalize it by means of two versions. The first one, of semantic nature, and allows us (under some computational hypotheses) to find true but unprovable statements in a logical system. Next, the syntactic version, closer to Gödel’s, allows us to find unprovable statements in formal systems. We finish the study of this theorem with some important mathematical and philosophical consequences.

Finally, we wrap up with some conclusions, and some final words for further work.
