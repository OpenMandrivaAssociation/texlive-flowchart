Name:		texlive-flowchart
Version:	36572
Release:	1
Summary:	Shapes for drawing flowcharts, using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/flowchart
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flowchart.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
