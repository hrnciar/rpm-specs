%global packname DelayedArray
%global packver 0.14.0

%global __suggests_exclude ^R\\((BiocStyle|DelayedMatrixStats|HDF5Array|airway|genefilter|pryr)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          Delayed operations on array-like objects
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-methods, R-stats4
BuildRequires:    R-BiocGenerics >= 0.31.5, R-S4Vectors-devel >= 0.25.15, R-IRanges-devel >= 2.17.3
BuildRequires:    R-matrixStats, R-BiocParallel

%description
Wrapping an array-like object (typically an on-disk object) in a DelayedArray
object allows one to perform common array operations on it without loading
the object in memory. In order to reduce memory usage and optimize
performance, operations on the object are either delayed or executed using a
block processing mechanism. Note that this also works on in-memory array-like
objects like DataFrame objects (typically with Rle columns), Matrix objects,
and ordinary arrays and data frames.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/unitTests
%{_libdir}/R/library/%{packname}/libs

%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.14.0-1
- update to 0.14.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.0-2
- Exclude Suggests for unavailable packages

* Tue Nov  5 2019 Tom Callaway <spot@fedoraproject.org> - 0.12.0-1
- update to 0.12.0 (now arch-specific)

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.4.1-1
- update to 0.4.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun  7 2017 Tom Callaway <spot@fedoraproject.org> - 0.2.7-1
- update to 0.2.7

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 0.2.4-1
- initial package
