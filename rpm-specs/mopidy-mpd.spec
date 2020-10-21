%global srcname Mopidy-MPD

Name:           mopidy-mpd
Version:        3.0.0
Release:        5%{?dist}
Summary:        Mopidy extension for controlling Mopidy from MPD clients

License:        ASL 2.0
URL:            https://mopidy.com/ext/mpd/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  mopidy
Requires:       mopidy

%description
Frontend that provides a full MPD server implementation to make Mopidy
available from MPD clients.


%prep
%autosetup -n %{srcname}-%{version}
rm MANIFEST.in

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/Mopidy_MPD-*.egg-info/
%{python3_sitelib}/mopidy_mpd/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 23 2020 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.0-4
- Explicitly BuildRequire setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.0-1
- Initial RPM Release

