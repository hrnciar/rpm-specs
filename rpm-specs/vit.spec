%global commit 7200949214362139e8073b6ca1a58cc756b2ebd0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout_date 20200430

%bcond_without tests
%global pypi_name vit

Name:           vit
Version:        2.0.0
Release:        7.%{checkout_date}git%{shortcommit}%{?dist}
Summary:        Visual Interactive Taskwarrior full-screen terminal interface


License:        MIT
URL:            https://github.com/scottkosty/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  task
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist urwid}
BuildRequires:  %{py3_dist tzlocal}
BuildRequires:  %{py3_dist tasklib}
BuildRequires:  %{py3_dist pytz}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
Features:
- Fully-customizable key bindings (default Vim-like)
- Uncluttered display
- No mouse
- Speed
- Per-column colorization
- Advanced tab completion
- Multiple/customizable themes
- Override/customize column formatters
- Intelligent sub-project indenting


%prep
%autosetup -n %{name}-%{commit}
rm -rf %{pypi_name}.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
find vit/ -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

# Install bashcompletion
install -d $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/
install -m 0644 -T scripts/bash/%{name}.bash_completion $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/vit

%check
%if %{with tests}
LC_ALL=C PYTHONPATH=. %{__python3} -m unittest
%endif

%files
%license LICENSE
%doc README.md CUSTOMIZE.md COLOR.md DEVELOPMENT.md UPGRADE.md
%{_bindir}/%{name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7.20200430git7200949
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6.20200430git7200949
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-5.20200430git7200949
- Update to latest upstream snapshot

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-3
- Include upgrade from github repo---not included in pypi tarball

* Mon Oct 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-2
- Update license
- Add UPGRADE.md

* Mon Oct 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-1
- Update to 2.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.8.0b2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.7.0b2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.6.0b2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0-0.5.0b2
- Update to beta 2
- Drop patch, merged upstream
- Remove requirements file, now included in pypi tar

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-0.4.0b1
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0-0.3.0b1
- Fix bash completion

* Sun Aug 04 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0-0.2.0b1
- Add patch to fix import bug
- Correct tests

* Sun Aug 04 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0-0.1.0b1
- Update to new version
- Moved to Python

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3-0.1.beta1
- Update to 1.3.beta1
- Remove unneeded patches
- Use github tarball
- Use make_build

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2-4
- Add BR: perl(Time::HiRes) (FT24FTBFS, RHBZ#1308231).
- Add %%license.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 11 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-1
- Update as per reviewer comments - rhbz1112072

* Tue Jun 24 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-1
- Update to new 1.2 stable version

* Mon Jun 23 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-0.1.beta1
- Initial rpmbuild
