%global packname  rsvg
%global rlibdir  %{_libdir}/R/library
%global with_suggests 0

Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Render SVG Images into PDF, PNG, PostScript, or Bitmap Arrays

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-spelling, R-svglite, R-magick, R-webp, R-ggplot2
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
%if %{with_suggests}
BuildRequires:    R-spelling
BuildRequires:    R-svglite
BuildRequires:    R-magick
BuildRequires:    R-webp
BuildRequires:    R-ggplot2
%endif
BuildRequires:    librsvg2-devel

%description
Renders vector-based svg images into high-quality custom-size bitmap arrays
using 'librsvg2'. The resulting bitmap can be written to e.g. png, jpeg or webp
format. In addition, the package can convert images directly to various formats
such as pdf or postscript.


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
%endif


%files
%dir %{rlibdir}/%{packname}
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/doc/
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.1-5
- update to 2.1
- conditionalize check around suggests (magick is not in Fedora)
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3-1
- initial package for Fedora
