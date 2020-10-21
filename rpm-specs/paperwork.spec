%global srcname paperwork

Name:           %{srcname}
Version:        1.3.1
Release:        5%{?dist}
Summary:        Using scanner and OCR to grep dead trees the easy way

License:        GPLv3+
URL:            https://github.com/openpaperwork/paperwork
Source0:        %pypi_source
Patch0001:      0001-Drop-extra-icon-dirs.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       hicolor-icon-theme
Requires:       python3-%{srcname} = %{version}-%{release}

%global _description %{expand: \
Paperwork is a personal document manager. It manages scanned documents and PDFs.

It's designed to be easy and fast to use. The idea behind Paperwork is "scan &
forget": You can just scan a new document and forget about it until the day you
need it again.

In other words, let the machine do most of the work for you.
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(paperwork-backend) >= 1.3
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pycountry)
BuildRequires:  python3dist(pyocr) >= 0.3
BuildRequires:  python3dist(pypillowfight)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(python-levenshtein)
BuildRequires:  python3dist(pyxdg) >= 0.25
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(termcolor)
BuildRequires:  python3-gobject
BuildRequires:  gtk3
BuildRequires:  gnome-icon-theme
BuildRequires:  libinsane-gobject
BuildRequires:  libnotify
BuildRequires:  tesseract
BuildRequires:  /usr/bin/xvfb-run

# Fallback to old orientation heuristic just freezes, so ensure this is
# available.
Requires:       tesseract-osd
Requires:       libinsane-gobject

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p2

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove spurious executable bit and shebangs.
sed -i -e '/^#!\//, 1d' src/%{srcname}/{,frontend/,frontend/import/,frontend/util/}__init__.py
sed -i -e '/^#!\//, 1d' src/%{srcname}/{deps,paperwork}.py


%build
%py3_build


%install
%py3_install

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    paperwork-shell install_system %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}

%find_lang %{srcname}


%check
paperwork-shell -b chkdeps paperwork_backend
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    xvfb-run -a paperwork-shell -b chkdeps paperwork

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/paperwork
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml

%files -n python3-%{srcname} -f %{name}.lang
%doc README.markdown
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove unused BuildRequires

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-3
- Require tesseract-osd so orientation detection doesn't freeze

* Tue Mar 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-2
- Fix icon installation

* Mon Mar 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Initial package.
