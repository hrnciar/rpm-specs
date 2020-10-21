%global common_description %{expand:
Ptpython is an advanced Python REPL built on top of the prompt_toolkit library.
It features syntax highlighting, multiline editing (the up arrow works),
autocompletion, mouse support, support for color schemes, support for bracketed
paste, both Vi and Emacs key bindings, support for double width (Chinese)
characters, and many other things.}


Name:           ptpython
Version:        3.0.2
Release:        3%{?dist}
Summary:        Python REPL build on top of prompt_toolkit
License:        BSD
URL:            https://github.com/prompt-toolkit/ptpython
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n ptpython3
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
Suggests:       %{py3_dist ipython}
Provides:       ptpython = %{version}-%{release}
Provides:       python3-ptpython = %{version}-%{release}
%{?python_provide:%python_provide python3-ptpython}


%description -n ptpython3 %{common_description}


%prep
%autosetup
rm -rf %{eggname}.egg-info
find -name \*.py | xargs sed -i -e '1 {/^#!\//d}'


%build
%py3_build


%install
%py3_install


%files -n ptpython3
%license LICENSE
%doc CHANGELOG README.rst
%{python3_sitelib}/ptpython
%{python3_sitelib}/ptpython-%{version}-py%{python3_version}.egg-info
%{_bindir}/ptpython
%{_bindir}/ptpython3
%{_bindir}/ptpython%{python3_version}
%{_bindir}/ptipython
%{_bindir}/ptipython3
%{_bindir}/ptipython%{python3_version}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Carl George <carl@george.computer> - 3.0.2-1
- Latest upstream rhbz#1760025
- Provide ptpython from ptpython3

* Tue Mar 24 2020 Carl George <carl@george.computer> - 2.0.6-1
- Update to 2.0.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Carl George <carl@george.computer> - 2.0.2-1
- Latest upstream
- Drop ptpython2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Carl George <carl@george.computer> - 0.41-7
- Add patch1 to fix Python 3.7 build (upstream #250)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.41-6
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.41-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Carl George <carl@george.computer> - 0.41-3
- Re-rebuild for F27

* Mon Sep 25 2017 Carl George <carl@george.computer> - 0.41-2
- Require python2-jedi

* Thu Jul 27 2017 Carl George <carl@george.computer> - 0.41-1
- Latest upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Carl George <carl.george@rackspace.com> - 0.39-1
- Latest upstream
- Add patch0 to undo https://github.com/jonathanslenders/ptpython/commit/16e4e31

* Sat Mar 18 2017 Carl George <carl.george@rackspace.com> - 0.36-1
- Initial package.
