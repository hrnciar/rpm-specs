%global packname  jqr
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          5%{?dist}
Summary:          Client for 'jq', a 'JSON' Processor

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-magrittr, R-lazyeval
# Suggests:  R-roxygen2 >= 6.1.0, R-jsonlite, R-testthat, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    jq-devel
BuildRequires:    R-magrittr
BuildRequires:    R-lazyeval
BuildRequires:    R-roxygen2 >= 6.1.0
BuildRequires:    R-jsonlite
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown

%description
Client for 'jq', a 'JSON' processor (<https://stedolan.github.io/jq/>),
written in C. 'jq' allows the following with 'JSON' data: index into,
parse, do calculations, cut up and filter, change key names and values,
perform conditionals and comparisons, and more.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# https://github.com/ropensci/jqr/commit/5d2c2f7a3688b0da8b3b99688da70b3df7385bb4
# Remove files pertaining to library bundling performed on CRAN.
rm inst/{AUTHORS,COPYING}.jq inst/jq_version
# Remove ignored files.
rm -r inst/ignore
popd

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
