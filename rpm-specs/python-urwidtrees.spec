%global srcname urwidtrees
%global sum Tree Widget Container API for the urwid toolkit
%global owner pazz
%global commit d1fa38ce4f37db00bdfc574b856023b5db4c7ead
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        1.0.2
Release:        7.git%{shortcommit}%{?dist}
Summary:        %{sum}

License:        GPLv3+
                # PyPI release is not maintained by pazz, so let's stick with github
URL:            https://github.com/%{owner}/%{srcname}
Source0:        https://github.com/%{owner}/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%description
It uses an MVC approach and allows to build trees of widgets. Its design
goals are

 * clear separation classes that define, decorate and display trees of widgets
 * representation of trees by local operations on node positions
 * easy to use default implementation for simple trees
 * Collapses are considered decoration


%package -n python3-%{srcname}
Requires:       python3-urwid
# there is `import urwidtrees` in setup.py, which results into `import urwid`
BuildRequires:  python3-urwid

Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
It uses an MVC approach and allows to build trees of widgets. Its design
goals are

 * clear separation classes that define, decorate and display trees of widgets
 * representation of trees by local operations on node positions
 * easy to use default implementation for simple trees
 * Collapses are considered decoration


%package -n python-%{srcname}-doc
BuildRequires:  python3-sphinx
Summary:        Documentation for %{srcname}
%description -n python-%{srcname}-doc
Development documentation for %{srcname}


%prep
%autosetup -n %{srcname}-%{commit}


%build
%py3_build
pushd docs/
make -e SPHINXBUILD=/usr/bin/sphinx-build-3 html
popd


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE.md
%{python3_sitelib}/*

%files -n python-%{srcname}-doc
%license LICENSE.md
%doc docs/build/html


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7.gitd1fa38c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-6.gitd1fa38c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5.gitd1fa38c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4.gitd1fa38c
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3.gitd1fa38c
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2.gitd1fa38c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Tomas Tomecek <ttomecek@redhat.com> - 1.0.2-1.gitd1fa38c
- latest upstream code: 1.0.2 d1fa38ce

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.gitfbcb183
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.gitfbcb183
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-8.gitfbcb183
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.gitfbcb183
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-6.gitfbcb183
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.gitfbcb183
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.gitfbcb183
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-3.gitfbcb183
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2.gitfbcb183
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Dec 10 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.0-1.gitfbcb183
- initial build

