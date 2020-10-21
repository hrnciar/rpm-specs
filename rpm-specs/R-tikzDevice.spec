%global packname tikzDevice
%global packver  0.12.3.1
%global rlibdir  %{_libdir}/R/library

# Some dependency loops.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.12.3.1
Release:          3%{?dist}
Summary:          R Graphics Output in LaTeX Format

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-filehash >= 2.3, R-png
# Suggests:  R-evaluate, R-formatR, R-ggplot2, R-knitr, R-lattice, R-maps, R-scales, R-stringr, R-testthat >= 0.8.1, R-withr
# LinkingTo:
# Enhances:

Requires:         texlive-pgf >= 2.0
Requires:         tex(preview.sty)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    texlive-pgf >= 2.0
BuildRequires:    tex(preview.sty)
BuildRequires:    R-filehash >= 2.3
BuildRequires:    R-png
BuildRequires:    R-evaluate
BuildRequires:    R-lattice
BuildRequires:    R-stringr
BuildRequires:    R-testthat >= 0.8.1
BuildRequires:    R-withr
%if %{with_suggests}
BuildRequires:    R-formatR
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-maps
BuildRequires:    R-scales
%endif

%description
Provides a graphics output device for R that records plots in a LaTeX-friendly
format. The device transforms plotting commands issued by R functions into
LaTeX code blocks. When included in a LaTeX document, these blocks are
interpreted with the help of 'TikZ'---a graphics package for TeX and friends
written by Till Tantau. Using the 'tikzDevice', the text of R plots can contain
LaTeX commands such as mathematical formula. The device also allows arbitrary
LaTeX code to be inserted into the output stream.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.utf8
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif


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


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.3.1-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.12.3-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.11-2
- rebuild for R 3.5.0

* Sat Mar 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10.1-1
- initial package for Fedora
