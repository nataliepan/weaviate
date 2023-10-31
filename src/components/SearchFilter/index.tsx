import React, { useState } from "react";
// import { styles } from "./styles";

const SearchFilter = (props: any) => {
  const { initialSearch, onSearch } = props;

  const [searchPhrase, setSearchPhrase] = useState(initialSearch || "");

  const handleInputChange = (event: any) => {
    setSearchPhrase(event.target.value);
    onSearch(event.target.value);
  };

  return (
    <div>
      <label className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">
        Search
      </label>
      <div className="relative  w-full max-w-xs">
        <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
          <svg
            className="w-4 h-4 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 20"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
            />
          </svg>
        </div>
        <input
          className="input input-bordered w-full max-w-xs pl-[35px]"
          id="name"
          type="text"
          placeholder="Search"
          value={searchPhrase}
          onChange={handleInputChange}
        />
      </div>
    </div>
  );
};

export default SearchFilter;
