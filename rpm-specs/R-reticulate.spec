%global packname reticulate
%global packver  1.16
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.16
Release:          2%{?dist}
Summary:          R Interface to 'Python'

License:          ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Skip-network-tests.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-jsonlite, R-Matrix, R-methods, R-rappdirs, R-Rcpp >= 0.12.7, R-utils
# Suggests:  R-callr, R-knitr, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

Requires:         python3
BuildRequires:    python3-devel
BuildRequires:    python3-docutils
BuildRequires:    python3-numpy
BuildRequires:    python3-pandas
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-jsonlite
BuildRequires:    R-Matrix
BuildRequires:    R-methods
BuildRequires:    R-rappdirs
BuildRequires:    R-Rcpp-devel >= 0.12.7
BuildRequires:    R-utils
BuildRequires:    R-callr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
# Test modules:
BuildRequires:   python3dist(docutils)
BuildRequires:   python3dist(matplotlib)
BuildRequires:   python3dist(numpy)
BuildRequires:   python3dist(pandas)
BuildRequires:   python3dist(scipy)

%description
Interface to Python modules, classes, and functions. When calling into Python,
R data types are automatically converted to their equivalent Python types. When
values are returned from Python to R they are converted back to R types.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Remove bundled byte-compiled files.
#rm inst/python/rpytools/*.pyc
rm -r inst/python/rpytools/__pycache__
sed -i '/pyc$/d' MD5

popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%py_byte_compile %{python3} %{buildroot}%{rlibdir}/%{packname}/python/rpytools


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/config
%{rlibdir}/%{packname}/python


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.16-2
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16-1
- Update to latest version

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12-1
- Update to latest version

* Sat Mar 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9-1
- Update to latest version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.7-2
- rebuild for R 3.5.0

* Sun Apr 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7-1
- Update to latest version

* Sun Apr 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-1
- initial package for Fedora
