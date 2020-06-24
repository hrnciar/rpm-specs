Name:             zathura-pdf-mupdf
Version:          0.3.5
Release:          2%{?dist}
Summary:          PDF support for zathura via mupdf
License:          zlib
URL:              http://pwmt.org/projects/zathura/plugins/%{name}
Source0:          http://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.xz
BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
BuildRequires:    jbig2dec-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    meson >= 0.43
BuildRequires:    mupdf-static >= 1.14
BuildRequires:    openjpeg2-devel
BuildRequires:    zathura-devel >= 0.3.9
Requires:         zathura >= 0.3.9
# Old plugins used alternatives
Conflicts:        zathura-pdf-poppler < 0.2.9

%description
This plugin adds PDF support to zathura using the mupdf rendering engine.

%prep
%setup -q

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
