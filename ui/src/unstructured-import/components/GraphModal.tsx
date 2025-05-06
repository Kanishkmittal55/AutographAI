import React from "react";

interface Props {
  logLines: string[];
  graphUrl: string | null;
  onClose: () => void;
}

const GraphModal: React.FC<Props> = ({ logLines, graphUrl, onClose }) => (
  <div className="fixed inset-0 z-50 bg-black bg-opacity-70 flex items-center justify-center">
    <div className="bg-gray-900 w-11/12 h-5/6 rounded-lg shadow-xl flex flex-col">
      {/* header */}
      <div className="flex justify-between items-center px-4 py-2 border-b border-gray-700">
        <h3 className="text-lg font-bold">Graph Build Activity</h3>
        <button onClick={onClose} className="text-gray-400 hover:text-white text-2xl leading-none">
          &times;
        </button>
      </div>

      {/* body */}
      <div className="flex flex-1 overflow-hidden">
        {/* logs */}
        <div className="w-1/3 bg-gray-800 p-4 overflow-auto text-xs">
          {logLines.map((l, i) => (
            <pre key={i} className="whitespace-pre-wrap">{l}</pre>
          ))}
        </div>

        {/* graph preview */}
        <div className="flex-1 bg-gray-900">
          {graphUrl ? (
            <iframe src={graphUrl} title="Graph" className="w-full h-full border-0" />
          ) : (
            <div className="h-full w-full flex items-center justify-center text-gray-500">
              Waiting for graph…
            </div>
          )}
        </div>
      </div>
    </div>
  </div>
);

export default GraphModal;
