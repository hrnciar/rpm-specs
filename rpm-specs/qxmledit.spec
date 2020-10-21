%global bigname QXmlEdit
Name:           qxmledit
Version:        0.9.15
Release:        4%{?dist}
# QXmlEdit - LGPLv2, some icons (oxygen) - GPLv3, QwtPlot3D - zlib-like
License:        LGPLv2+ and GPLv3 and zlib
Summary:        Simple XML Editor and XSD Viewer
Url:            http://qxmledit.org/
Source:         https://github.com/lbellonda/qxmledit/archive/%{version}/%{name}-%{version}.tar.gz
# desktop things (https://github.com/lbellonda/qxmledit/issues/71)
Patch0:         %{name}-%{version}-install.diff
# ordinar lib names (https://github.com/lbellonda/qxmledit/issues/73)
Patch1:         %{name}-%{version}-libsuffix.diff
# default installation paths (https://github.com/lbellonda/qxmledit/issues/75)
Patch2:         %{name}-%{version}-paths.diff
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt5-linguist
# qt5-qtbase-devel (Qt5Core..Qt5Xml)
BuildRequires:  pkgconfig(Qt5)
# qt5-qtsvg-devel
BuildRequires:  pkgconfig(Qt5Svg)
# qt5-qtscxml-devel
BuildRequires:  pkgconfig(Qt5Scxml)
# qt5-qtxmlpatterns-devel
BuildRequires:  pkgconfig(Qt5XmlPatterns)
# qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(Qt5Qml)
# mesa-libGLU-devel
BuildRequires:  pkgconfig(glu)
Requires:       libqxmledit%{?_isa} = %{version}-%{release}

%description
QXmlEdit is a simple XML editor based on qt libraries. Its main features are
unusual data visualization modes, nice XML manipulation and presentation and it
is multi platform. It can split very big XML files into fragments, and compare
XML files. It is one of the few graphical Open Source XSD viewers.

%package        doc
Summary:        Simple XML Editor documentatio
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit documentation.

%package -n     libqxmledit
Summary:        XML Editor Shared Libraries

%description -n libqxmledit
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit shared libraries.

%package -n     libqxmledit-devel
Summary:        XML Editor Development Files
Requires:       libqxmledit%{?_isa} = %{version}-%{release}

%description -n libqxmledit-devel
QXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit development files.


%prep
%autosetup -p 0
# tmp fix (https://github.com/lbellonda/qxmledit/issues/74)
desktop-file-edit --add-mime-type=application/xml install_scripts/environment/desktop/%{bigname}.desktop


%build
lrelease-qt5 {src/QXmlEdit.pro,src/QXmlEditWidget.pro,src/sessions/QXmlEditSessions.pro}
%{qmake_qt5} \
    PREFIX=%{_prefix} \
    QXMLEDIT_INST_LIB_DIR=%{_libdir} \
    QXMLEDIT_INST_USE_C11=y
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}
# Install icons.
install -Dm 0644 install_scripts/environment/icon/qxmledit_48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm 0644 src/images/icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# Install a manual page.
install -Dm 0644 install_scripts/environment/man/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1
# i18n
%find_lang %{bigname} --with-qt --without-mo
%find_lang {%{bigname},QXmlEditWidget,SCXML,QXmlEditSessions} --with-qt --without-mo


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bigname}.desktop


%files -f %{bigname}.lang
%license COPYING GPLV3.txt LGPLV3.txt
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{bigname}.desktop
%{_datadir}/appdata/%{bigname}.appdata.xml
%{_datadir}/icons/hicolor/{32x32,48x48,scalable}/apps/%{name}.*
%{_mandir}/man1/%{name}.1.*

%files doc
%license COPYING GPLV3.txt LGPLV3.txt
%{_datadir}/doc/%{name}/QXmlEdit_manual.pdf

%files -n libqxmledit
%license COPYING GPLV3.txt LGPLV3.txt
%{_libdir}/libQXmlEdit{Sessions,Widget}.so.0*

%files -n libqxmledit-devel
%license COPYING GPLV3.txt LGPLV3.txt
%{_includedir}/%{name}/
%{_libdir}/libQXmlEdit{Sessions,Widget}.so


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-3
- Spec fixes

* Sun Jul 05 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-2
- Spec fixes

* Tue Jun 09 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-1
- Initial packaging
