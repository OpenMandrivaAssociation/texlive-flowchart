# revision 29153
# category Package
# catalog-ctan /graphics/pgf/contrib/flowchart
# catalog-date 2013-02-18 18:17:35 +0100
# catalog-license lppl1.3
# catalog-version 3.2
Name:		texlive-flowchart
Version:	3.2
Release:	2
Summary:	Shapes for drawing flowcharts, using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/flowchart
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of 'traditional' flowchart element
shapes; the documentation shows how to build a flowchart from
these elements, using pgf/TikZ. The package also requires the
makeshape package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flowchart/flowchart.sty
%doc %{_texmfdistdir}/doc/latex/flowchart/README
%doc %{_texmfdistdir}/doc/latex/flowchart/flowchart.pdf
#- source
%doc %{_texmfdistdir}/source/latex/flowchart/flowchart.dtx
%doc %{_texmfdistdir}/source/latex/flowchart/flowchart.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
