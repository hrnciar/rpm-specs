# Desired jbig2dec header files and library version
# Apparantly, jbig2dec complains even about newer versions.
# Please update if needed.
%global jbig2dec_version 0.19

Name:             zathura-pdf-mupdf

Version:          0.3.6
Release:          4%{?dist}
Summary:          PDF support for zathura via mupdf
License:          zlib
URL:              https://pwmt.org/projects/%{name}/
Source0:          %{url}/download/%{name}-%{version}.tar.xz
Patch0:           0001-link-against-gumbo-for-mupdf-1.18.patch
BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    meson >= 0.43
BuildRequires:    mupdf-static >= 1.17
BuildRequires:    openjpeg2-devel
BuildRequires:    zathura-devel >= 0.3.9
BuildRequires:    gumbo-parser-devel
Requires:         zathura >= 0.3.9
# Depend on exact versions like mupdf does
# https://src.fedoraproject.org/rpms/mupdf/c/02d93ee0f097415aa095ffcea4d768e5f43fac91?branch=master
BuildRequires:  jbig2dec-devel = %{jbig2dec_version}
BuildRequires:  jbig2dec-libs = %{jbig2dec_version}
Requires:       jbig2dec-libs = %{jbig2dec_version}

# Old plugins used alternatives
Conflicts:        zathura-pdf-poppler < 0.2.9

%description
This plugin adds PDF support to zathura using the mupdf rendering engine.

%prep
%autosetup

%build
%meson -Dlink-external=true
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

# Clean the old alternatives link
%pre
[ -L %{_libdir}/zathura/pdf.so ] && rm -f %{_libdir}/zathura/pdf.so || :

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/applications/org.pwmt.zathura-pdf-mupdf.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml

%changelog
* Fri Oct 09 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-4
- link against gumbo

* Thu Oct 08 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-3
- rebuild for mupdf 1.18.0

* Fri Sep 18 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-2
- rebuild with jbig2dec 0.19

* Mon Sep 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.6-1
- Update to new release

* Tue Jul 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-4
- Rebuild to require exact jgib2dec version
- #1860987

* Sat May 16 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.5-3
- Adjust to mupdf 1.17

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-1
- Update to 0.3.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Petr Šabata <contyk@redhat.com> - 0.3.4-1
- 0.3.4 bump
- Fixes rhbz#1645552

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Petr Šabata <contyk@redhat.com> - 0.3.3-1
- 0.3.3 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Petr Šabata <contyk@redhat.com> - 0.3.1-1
- 0.3.1 bump
- Don't link against the no longer provided libmupdfthird,
  see rhbz#1438824 for more info

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-3
- Rebuild against mujs-0-6.20161031gita0ceaf5

* Thu Sep 29 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-2
- Rebuild against mujs-0-5.20160921git5c337af

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-4
- Rebuild with mujs-0-1.20150929git0827611

* Wed Jul 01 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-3
- Handle the desktop file properly

* Tue Jun 23 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-2
- Correct the %%files section

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-1
- Initial packaging
