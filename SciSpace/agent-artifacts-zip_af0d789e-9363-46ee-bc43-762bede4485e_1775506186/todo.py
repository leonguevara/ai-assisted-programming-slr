Planner Code plan:
```python
def main():
    # 1. Read the existing SLR markdown report from /home/sandbox/SLR_AI_Code_Generation_Detailed_Report.md
    # 2. Process the markdown content to extract sections (Abstract, Introduction, RQs, Methodology, Results, Discussion, Conclusion)
    # 3. Format the content into a complete IEEEtran LaTeX template for IEEE Transactions on Software Engineering
    # 4. Extract all 30 references and format them into a BibTeX (.bib) file
    # 5. Write the LaTeX content to /home/sandbox/manuscript.tex using filesystem_file_write
    # 6. Write the BibTeX content to /home/sandbox/references.bib using filesystem_file_write
    # 7. Compile the document using bash_run_command with the sequence:
    #    a. pdflatex -interaction=nonstopmode manuscript.tex
    #    b. bibtex manuscript
    #    c. pdflatex -interaction=nonstopmode manuscript.tex
    #    d. pdflatex -interaction=nonstopmode manuscript.tex
    # 8. Verify the successful generation of /home/sandbox/manuscript.pdf and confirm its existence
    
if __name__ == "__main__":
    main()
```