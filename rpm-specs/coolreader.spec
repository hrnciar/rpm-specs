Summary: Cross platform open source e-book reader
Name: coolreader
Version: 3.2.34
Release: 2%{?dist}
License: GPLv2
URL: https://sourceforge.net/projects/crengine
Source0: https://github.com/buggins/coolreader/archive/cr%{version}/coolreader-cr%{version}.tar.gz
Source1: cr3.appdata.xml

Patch0: coolreader-0001-fix-paths-in-a-cr3.desktop-file.patch
# https://github.com/buggins/coolreader/issues/80
Patch1: coolreader-0002-add-license-file.patch

BuildRequires: gcc-c++
BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtGui)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
CoolReader is fast and small cross-platform XML/CSS based eBook reader for
desktops and handheld devices. Supported formats: FB2, TXT, RTF, DOC, TCR,
HTML, EPUB, CHM, PDB, MOBI.

%prep
%autosetup -p1 -n %{name}-cr%{version}
%cmake \
	-DGUI=QT \
	-DMAX_IMAGE_SCALE_MUL=2 \
	-DDOC_DATA_COMPRESSION_LEVEL=3 \
	-DDOC_BUFFER_SIZE=0x140000 \
        .

%build
%make_build

%install
%make_install
install -D -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/cr3.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cr3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/cr3.appdata.xml

%files
%license LICENSE
%{_bindir}/cr3
%{_datadir}/applications/cr3.desktop
%{_metainfodir}/cr3.appdata.xml
%{_datadir}/cr3
%{_datadir}/pixmaps/cr3.*
%{_mandir}/man1/cr3.1*
%doc %{_docdir}/cr3
%doc README.md

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.34-1
- Update to 3.2.34

* Wed Nov 06 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.33-1
- Update to 3.2.33

* Mon Oct 07 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.32-1
- Update to 3.2.32

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.30-1
- Update to 3.2.30

* Sun Feb 24 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.29-1
- Initial package
