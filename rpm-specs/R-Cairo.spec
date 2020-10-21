%global packname Cairo
%global packver  1.5-12.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.5.12.2
Release:          2%{?dist}
Summary:          Use Cairo for high-quality bitmap, vector, and display output

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-graphics
# Suggests:  R-png
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-graphics
BuildRequires:    R-png
BuildRequires:    cairo-devel >= 1.2
BuildRequires:    libXt-devel

%description
R graphics device using cairographics library that can be used to create
high-quality vector (PDF, PostScript and SVG) and bitmap output (PNG, JPEG,
TIFF), and high-quality rendering in displays (X11 and Win32).  Since it uses
the same back-end for all output, copying across formats is WYSIWYG. Files are
created without the dependence on X11 or other external programs. This device
supports alpha channel (semi-transparent drawing) and resulting images can
contain transparent and semi-transparent regions. It is ideal for use in server
environments (file output) and as a replacement for other devices that don't
have Cairo's capabilities such as alpha support or anti-aliasing. Backends are
modular such that any subset of backends is supported.


%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12.2-1
- Update to latest version

* Thu Jun 25 2020 José Abílio Matos <jamatos@fc.up.pt> - 1.5.12-3
- bump version to ensure upgrade path (due to a F32 rebuild)

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.12-2
- Rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12-1
- Update to latest version

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.11-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-2
- Cleanup summary and description

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.5.9-4
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.9-2
- Cleanup metadata a bit.

* Fri Feb 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.9-1
- initial package for Fedora
