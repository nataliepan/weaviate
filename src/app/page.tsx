"use client";
import SearchFilter from "@/components/SearchFilter";
import React, { useEffect, useState } from "react";

interface Item {
  image: string;
  desc: string;
  title: string;
  price: string;
}

export default function Home() {
  const [search, setSearch] = useState("");
  const [data, setData] = useState([] as Item[]);
  const onSearch = () => {
    console.log("search", search);
  };

  useEffect(() => {
    fetch("/api/json")
      .then((res) => res.json())
      .then((data) => {
        console.log(data.message);

        setData([
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
          {
            image: "/source/image/Mustard_Tweed.jpeg",
            desc: "Beautiful and rare Mid-Century Modern Adrian Pearsall for Craft Associates Gondola sofa with walnut legs and mustard yellow upholstery. The tweeted yellow fabric is in great condition and can be used as-is. Tufted detailing throughout. The sofa has only had one owner and has had very little use. This sofa can blend into many styles of decoration, including mid- century, boho, modern and eclectic.",
            title: "Adrian Pearsall Gondola Sofa for Craft Associates in Mustard Tweed - $7,500",
            price: "$7,500",
          },
        ]);
      });
  }, []);

  return (
    <main className="h-screen w-screen flex justify-center items-center">
      <div className="form-control w-full m-auto p-4">
        <div className="flex flex-row py-2 w-full m-auto max-w-sm">
          <SearchFilter onSearch={setSearch} initialSearch={search} />{" "}
          <button className="ml-2 btn btn-primary" onClick={onSearch}>
            Search
          </button>
        </div>
        <div className="grid grid-cols-4 gap-4">
          {data.map((item, index) => (
            <div className="card card-compact bg-base-100 shadow-xl">
              <figure>
                <img src="/source/image/Mustard_Tweed.jpeg" alt="Couch" />
              </figure>
              <div className="card-body">
                <h2 className="card-title">Shoes!</h2>
                <p>If a dog chews shoes whose shoes does he choose?</p>
                {/* <div className="card-actions justify-end">
                <button className="btn btn-primary">Buy Now</button>
              </div> */}
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
