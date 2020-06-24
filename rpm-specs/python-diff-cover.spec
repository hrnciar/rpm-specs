%global desc Diff coverage is the percentage of new or modified lines that are covered by \
tests. This provides a clear and achievable standard for code review: If you \
touch a line of code, that line should be covered. Code coverage is *every* \
developer's responsibility! \
\
The diff-cover command line tool compares an XML coverage report with the \
output of git diff. It then reports coverage information for lines in the \
diff.


Name:           python-diff-cover
Version:        3.0.0
Release:        1%{?dist}
BuildArch:      noarch

License:        ASL 2.0
Summary:        Automatically find diff lines that need test coverage
URL:            https://github.com/Bachmann1234/diff-cover/
Source0:        %{url}/archive/v%{version}/diff-cover-%{version}.tar.gz


# Some of the python3 BuildRequires are needed so we can run the entry point scripts for help2man
BuildRequires:  /usr/bin/flake8
BuildRequires:  /usr/bin/pycodestyle
BuildRequires:  /usr/bin/pylint
BuildRequires:  git
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2 >= 2.7.1
BuildRequires:  python3-jinja2_pluralize
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pygments >= 2.0.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.6.1


%description
%{desc}


%package -n python3-diff-cover
Summary:        %{summary}

# needed for the _git_root test
Requires:       git
# Required for the entry_point scripts
Requires:       python3-setuptools
# from requirements.txt
Requires:       python3-jinja2 >= 2.7.1
Requires:       python3-jinja2_pluralize
Requires:       python3-pygments >= 2.0.1
Requires:       python3-six >= 1.6.1


%{?python_provide:%python_provide python3-diff-cover}


%description -n python3-diff-cover
%{desc}


%prep
%autosetup -n diff_cover-%{version}
rm -rf diff_cover.egg-info


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-cover %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-cover.1 \
        %{buildroot}%{_bindir}/diff-cover

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-quality %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-quality.1 \
        %{buildroot}%{_bindir}/diff-quality


%check
# Two tests fail: https://github.com/Bachmann1234/diff_cover/issues/136
pytest-3 -k "not test_html_with_external_css and not test_load_declared_arabic"


%files -n python3-diff-cover
%license LICENSE
%doc README.rst
%{_bindir}/diff-cover
%{_bindir}/diff-quality
%{_mandir}/man1/diff-cover.1*
%{_mandir}/man1/diff-quality.1*
%{python3_sitelib}/diff_cover
%{python3_sitelib}/diff_cover-%{version}-*.egg-info


%changelog
* Wed Jun 03 2020 Clément Verna <cverna@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 RHBZ#1821943
- https://github.com/Bachmann1234/diff_cover/blob/v3.0.0/CHANGELOG

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 (#1800860).
- https://github.com/Bachmann1234/diff_cover/blob/v2.6.0/CHANGELOG

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2 (#1783722).
- https://github.com/Bachmann1234/diff_cover/blob/v2.5.2/CHANGELOG

* Thu Nov 21 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1 (#1774828).
- https://github.com/Bachmann1234/diff_cover/blob/v2.4.1/CHANGELOG

* Fri Nov 15 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0 (#1762995).
- https://github.com/Bachmann1234/diff_cover/blob/V2.4.0/CHANGELOG

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 2.3.0-1
- Update to 2.3.0. Fixes bug #1725493

* Tue Jun 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (#1720455).
- https://github.com/Bachmann1234/diff-cover/blob/v2.2.0/CHANGELOG

* Tue Jun 04 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (#1697689).
- https://github.com/Bachmann1234/diff-cover/blob/v2.1.0/CHANGELOG

* Wed Apr 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (#1689572).
- https://github.com/Bachmann1234/diff-cover/blob/v1.0.7/CHANGELOG

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5.

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.12-5
- Subpackage python2-diff-cover has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.12-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
