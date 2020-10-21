%global pname   controlyourtabs
%global uuid    com.thingsthemselves.gedit.plugins.%{pname}

Name:           gedit-control-your-tabs
Version:        0.3.3
Release:        2%{?dist}
Summary:        Gedit plugin to switch between document tabs using

License:        GPLv3+
URL:            https://github.com/jefferyto/gedit-control-your-tabs
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       gedit%{?_isa} >= 3.8

Provides:       bundled(python-gtk-utils) = 0.2.0

%description
A gedit plugin to switch between document tabs using Ctrl+Tab / Ctrl+Shift+Tab
(most recently used order or tab row order) and Ctrl+PageUp / Ctrl+PageDown (tab
row order).


%prep
%autosetup -p1


%install
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{pname}          %{buildroot}%{_libdir}/gedit/plugins/
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/schemas
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/utils/.editorconfig
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/utils/.gitattributes
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/locale
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{pname}.plugin   %{buildroot}%{_libdir}/gedit/plugins/
mkdir -p                %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -a %{pname}/schemas/%{uuid}.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/

# Byte compiling
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/%{pname}/

# Install metainfo
install -m 0644 -Dp data/%{uuid}.metainfo.xml %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_libdir}/gedit/plugins/%{pname}
%{_libdir}/gedit/plugins/%{pname}.plugin
%{_metainfodir}/*.xml


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9.20190807git3064a92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-8.20190807git3064a92
- Add AppData manifest file

* Mon Jul 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-7.20190225gitd594f75
- Remove 'noarch'

* Mon Jul 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-6.20190225gitd594f75
- py_byte_compile path fix

* Thu Jul 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-5.20190225gitd594f75
- Initial package
