%global commit 88c53cd44a626ede3b07dab0b548f8bcfda42867
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          pycanberra
Summary:       A very basic (and incomplete) wrapper for libcanberra
URL:           https://github.com/psykoyiko/pycanberra/
License:       LGPLv2

# There's no versioning upstream, it's all about the Git hash
Version:       0
Release:       0.24.git%{shortcommit}%{?dist}

# There aren't any release yet, I'm downloading straight from the last commit
Source0:       https://github.com/psykoyiko/pycanberra/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:     noarch

BuildRequires: python3-devel

# This will break at run time when libcanberra bumps its soname :(
Requires:      libcanberra

%description
A very basic (and incomplete) wrapper of libcanberra for Python 2.


%package -n python3-canberra
Summary:       A very basic (and incomplete) wrapper for libcanberra

%description -n python3-canberra
A very basic (and incomplete) wrapper of libcanberra for Python 3.


%prep
%setup -q -n pycanberra-%{commit}


%build
# Nothing to build


%install
install -D -p -m 0644 pycanberra.py -t %{buildroot}%{python3_sitelib}/


%files -n python3-canberra
%doc COPYING README
%{python3_sitelib}/pycanberra.py
%{python3_sitelib}/__pycache__/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.24.git88c53cd
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.22.git88c53cd
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.21.git88c53cd
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0-0.18.git.git88c53cd
- Drop python2 subpackage (#1625773)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0-0.16.git88c53cd
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0-0.12.git88c53cd
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git88c53cd
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Orion Poplawski <orion@cora.nwra.com> - 0-0.9.git88c53cd
- Fix files for python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git88c53cd
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 10 2015 Mathieu Bridon <bochecha@daitauha.fr> - 0-0.8.git65c3b3f
- New snapshot from master.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git65c3b3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git65c3b3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0-0.5.git65c3b3f
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git65c3b3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0-0.3.git65c3b3f
- Add a python3 subpackage.

* Tue Oct 02 2012 Mathieu Bridon <bochecha@fedoraproject.org> - 0-0.2.git65c3b3f
- Fix requirement on libcanberra.

* Wed Sep 26 2012 Mathieu Bridon <bochecha@fedoraproject.org> - 0-0.1.git65c3b3f
- Initial package for Fedora.
