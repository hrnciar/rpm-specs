Name:		inkscape-psd
Version:	0.1.1
Release:	12%{?dist}
Summary:	Inkscape PSD Importer
License:	BSD
URL:		http://pernsteiner.org/inkscape/psd_import/
Source:		http://pernsteiner.org/inkscape/psd_import/inkscape-psd_import-%{version}.zip
Patch0:         inkscape-psd-python3.patch
Requires:	inkscape
Requires:	python3
BuildArch:	noarch

%description
This Inkscape extension allows you to load Photoshop PSD files.

%prep
%setup -q -c %{name}-%{version}

%patch0 -p1

# Documentation of Licence (as it written in every file) :
ln -s %{_datadir}/inkscape/extensions/psd_import/__init__.py LICENSE

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
cp -p psd_import.inx %{buildroot}%{_datadir}/inkscape/extensions
cp -p psd_import_main.py %{buildroot}%{_datadir}/inkscape/extensions
cp -rp psd_import %{buildroot}%{_datadir}/inkscape/extensions

%files
%license LICENSE
%{_datadir}/inkscape/extensions/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.1-11
- Port to Python 3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 2 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.1-2
- Remove un-needed %%doc
- Add python as a require
- New way to documentation of LICENSE

* Fri Apr 3 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.1-1
- Initial build
