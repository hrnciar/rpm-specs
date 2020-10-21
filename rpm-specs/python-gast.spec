Name:           python-gast
Version:        0.4.0
Release:        1%{?dist}
Summary:        Python AST that abstracts the underlying Python version
License:        BSD
URL:            https://github.com/serge-sans-paille/gast/
Source0:        %{url}/archive/%{version}/gast-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.}
%description %_description


%package -n     python3-gast
Summary:        %{summary}

%description -n python3-gast %_description


%prep
%autosetup -p1 -n gast-%{version}

# https://github.com/serge-sans-paille/gast/pull/52
sed -i -e 's/ --pep8//' -e 's/pytest-pep8/pytest/' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gast


%check
%tox


%files -n python3-gast -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Fri Sep 11 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-1
- Update to 0.4.0
- Fixes rhbz#1878159

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-1
- Update to 0.3.3 (#1844892)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jan 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-1
- Initial package
