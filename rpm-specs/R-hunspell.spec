%global packname  hunspell
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((janeaustenr|stopwords|wordcloud2)\\)

# Dependency loops.
%global with_suggests 0
# Some examples use network to download stuff.
%bcond_with network 0

Name:             R-%{packname}
Version:          3.0
Release:          5%{?dist}
Summary:          High-Performance Stemmer, Tokenizer, and Spell Checker

License:          GPLv2 or LGPLv2 or MPLv1.1
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp, R-digest
# Suggests:  R-spelling, R-testthat, R-pdftools, R-janeaustenr, R-wordcloud2, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-digest
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-pdftools
%if %{with_suggests}
BuildRequires:    R-spelling
BuildRequires:    R-janeaustenr
BuildRequires:    R-wordcloud2
%endif

# Not currently possible to unbundle at the moment.
# https://github.com/ropensci/hunspell/issues/34
Provides: bundled(hunspell) = 1.7.0

%description
Low level spell checker and morphological analyzer based on the famous
'hunspell' library <https://hunspell.github.io>. The package can analyze
or check individual words as well as parse text, latex, html or xml
documents. For a more user-friendly interface use the 'spelling' package
which builds on this package to automate checking of files, documentation
and vignettes in all common formats.


%prep
%setup -q -c -n %{packname}

# Fix executable bits.
chmod -x %{packname}/inst/dict/*.{aff,dic}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# Can't run spell check with dependency loop.
%if !%{with_suggests}
rm %{packname}/tests/spelling.R
%endif

export LANG=C.UTF-8
# Skip vignettes using the network.
%if !%{with network}
ARGS="--no-examples --no-vignettes"
%endif
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} $ARGS
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} $ARGS
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/AUTHORS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/dict
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org> - 3.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.9-1
- initial package for Fedora
