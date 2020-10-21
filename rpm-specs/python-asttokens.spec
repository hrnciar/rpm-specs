Name:           python-asttokens
Version:        2.0.4
Release:        2%{?dist}
Summary:        Module to annotate Python abstract syntax trees with source code positions

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/asttokens
Source0:        https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(astroid)
BuildRequires:  python3dist(six)

%global _description %{expand:
The asttokens module annotates Python abstract syntax trees (ASTs)
with the positions of tokens and text in the source code that
generated them. This makes it possible for tools that work with
logical AST nodes to find the particular text that resulted in those
nodes, for example for automated refactoring or highlighting.}

%description %_description

%package     -n python3-asttokens
Summary:        %{summary}
Requires:       %{py3_dist six}
%{?python_provide:%python_provide python3-asttokens}

%description -n python3-asttokens %_description

%prep
%autosetup -p1 -n asttokens-%{version}

%build
%py3_build

%install
%py3_install

%check
# Failing tests: https://github.com/gristlabs/asttokens/issues/59
pytest-3 tests/ -v --ignore=tests/testdata/ \
  --deselect=tests/test_astroid.py::TestAstroid::test_fixture9 \
  --deselect=tests/test_astroid.py::TestAstroid::test_splat \
  --deselect=tests/test_astroid.py::TestAstroid::test_sys_modules \
  --deselect=tests/test_mark_tokens.py::TestMarkTokens::test_fixture9 \
  --deselect=tests/test_mark_tokens.py::TestMarkTokens::test_splat \
  --deselect=tests/test_mark_tokens.py::TestMarkTokens::test_sys_modules

%files -n python3-asttokens
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.4-1
- Update to latest version (#1823090)
- Ignore tests that fail with python3.9 (#1817679)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019  <zbyszek@in.waw.pl> - 2.0.3-1
- Update to latest bugfix release

* Tue Oct 15 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-1
- Update to latest version (#1752074). This should finally fix compatibility
  with python3.8.

* Tue Sep 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.13-3
- Fix build with python3.8 (#1697503)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May  4 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.13-1
- Update to latest version (#1697407)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.10-4
- Subpackage python2-asttokens has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.10-2
- Replace my own patches with better patches from upstream
  (all tests should now pass)

* Thu Jul  5 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.10-1
- Update to latest version (#1586009)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.6-1
- Initial version
