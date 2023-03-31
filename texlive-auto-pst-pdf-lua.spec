Name:		texlive-auto-pst-pdf-lua
Version:	54779
Release:	2
Summary:	Using LuaLaTeX together with PostScript code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/auto-pst-pdf-lua
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf-lua.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auto-pst-pdf-lua.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a slightly modified version of auto-pst-pdf by
Will Robertson, which itself is a wrapper for pst-pdf by Rolf
Niepraschk. The package allows the use of LuaLaTeX together
with PostScript related code, eg. PSTricks. It depends on
ifpdf, ifluatex, ifplatform, and xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/auto-pst-pdf-lua
%doc %{_texmfdistdir}/doc/latex/auto-pst-pdf-lua

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
