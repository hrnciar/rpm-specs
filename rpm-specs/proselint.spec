Name:           proselint
Version:        0.10.2
Release:        7%{?dist}
Summary:        A linter for English prose

License:        BSD
URL:            http://proselint.com/
Source0:        %pypi_source
BuildArch:      noarch

Requires:       python3-click
Requires:       python3-future
Requires:       python3-six

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For running the tests:
BuildRequires:  python3-click
BuildRequires:  python3-future
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-six


%description
proselint's goal is to aggregate knowledge about best practices in
writing and to make that knowledge immediately accessible to all authors
in the form of a linter for prose.  It is a command-line utility that
can be integrated into existing tools.


%prep
%autosetup -p 1 -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}%{python3_sitelib}/%{name}/.%{name}rc \
   %{buildroot}%{_sysconfdir}/%{name}rc


%check
env PATH=%{buildroot}%{_bindir}:$PATH \
    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    LANG=C.UTF-8 \
    pytest-%{python3_version}


%files
%config(noreplace) %{_sysconfdir}/%{name}rc
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug  4 2018 Peter Oliver <rpm@mavit.org.uk> - 0.10.2-1
- Update to version 0.10.2.

* Tue Jul 24 2018 Peter Oliver <rpm@mavit.org.uk> - 0.10.0-1
- Update to version 0.10.0.
- Work around https://github.com/amperser/proselint/issues/867 by
  fetching source directly from GitHub.

* Sun Jul 22 2018 Peter Oliver <rpm@mavit.org.uk> - 0.9.0-1
- Update to version 0.9.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Peter Oliver <rpm@mavit.org.uk> - 0.8.0-4
- Tweak URL and summary.

* Fri Aug 25 2017 Peter Oliver <rpm@mavit.org.uk> - 0.8.0-3
- Drop separate library packages, and rename to `proselint`.
- Lint fixes.

* Wed Jun 28 2017 Peter Oliver <rpm@mavit.org.uk> - 0.8.0-2
- Name "python2" in more dependencies, where possible.
- Fix typo.

* Thu Feb 23 2017 Peter Oliver <rpm@mavit.org.uk> - 0.8.0-1
- Update to 0.8.0.

* Sun Oct 09 2016 Peter Oliver <rpm@mavit.org.uk> - 0.7.0-1
- Initial package, assisted by pyp2rpm-3.1.3.
