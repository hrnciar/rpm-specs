Name:           playitagainsam
Version:        0.5.0
Release:        13%{?dist}
Summary:        Record and replay interactive terminal sessions

License:        MIT
URL:            https://github.com/rfk/playitagainsam
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-psutil >= 2.0
Requires:       python3-six

# shortcut and executable name
Provides:       pias = %{version}-%{release}

%description
Playitagainsam is a tool and a corresponding file format for recording and
replaying interactive terminal sessions. It takes inspiration from the Unix
commands "script" and "ttyrec" and the Python tool "playerpiano".

Useful features include:

 * ability to replay with fake typing for enhanced "interactivity"
 * ability to replay synchronized output in multiple terminals

%prep
%autosetup -n %{name}-%{version}

# Shebang removal
sed -i '1d' %{name}/__main__.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.rst ChangeLog.txt
%{_bindir}/pias
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuild for Python 3.6

* Thu Nov 24 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-1
- Initial package
