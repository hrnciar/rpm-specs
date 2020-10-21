%global packname downlit
%global packver  0.2.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Syntax Highlighting and Automatic Linking

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-brio, R-digest, R-evaluate, R-fansi, R-rlang, R-vctrs, R-yaml
# Suggests:  R-rmarkdown, R-jsonlite, R-MASS, R-testthat, R-covr, R-pkgload, R-xml2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-brio
BuildRequires:    R-digest
BuildRequires:    R-evaluate
BuildRequires:    R-fansi
BuildRequires:    R-rlang
BuildRequires:    R-vctrs
BuildRequires:    R-yaml
BuildRequires:    R-rmarkdown
BuildRequires:    R-jsonlite
BuildRequires:    R-MASS
BuildRequires:    R-testthat
BuildRequires:    R-pkgload
BuildRequires:    R-xml2

%description
Syntax highlighting of R code, specifically designed for the needs of RMarkdown
packages like pkgdown, hugodown, and bookdown. It includes linking of function
calls to their documentation on the web, and automatic translation of ANSI
escapes in output to the equivalent HTML.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Fri Sep 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Update to latest version (#1882612)

* Tue Sep 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora
