%global packname  pdftools
%global rlibdir  %{_libdir}/R/library
%global with_suggests 0

Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Text Extraction, Rendering and Converting of PDF Documents

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-qpdf
# Suggests:  R-jpeg, R-png, R-webp, R-tesseract, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-qpdf
BuildRequires:    poppler-cpp-devel
BuildRequires:    poppler-data
BuildRequires:    R-jpeg
BuildRequires:    R-png
BuildRequires:    R-webp
BuildRequires:    R-testthat
%if %{with_suggests}
BuildRequires:    R-tesseract
%endif

%description
Utilities based on 'libpoppler' for extracting text, fonts, attachments
and metadata from a PDF file. Also supports high quality rendering of PDF
documents into PNG, JPEG, TIFF format, or into raw bitmap vectors for
further processing in R.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org> - 2.2-6
- update to 2.3.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.2-4
- Rebuild for poppler-0.84.0

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.7-1
- update to 1.7

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-1
- Update to latest version

* Mon Mar 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-2
- Add missing Rcpp Requires

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-1
- initial package for Fedora
