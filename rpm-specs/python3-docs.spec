Name:           python3-docs
Summary:        Documentation for the Python 3 programming language

# The Version should be in-sync with the python3 package:
%global         pybasever 3.9
%global         general_version %{pybasever}.0
#global         prerel ...
%global         upstream_version %{general_version}%{?prerel}
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
License:        Python
URL:            https://www.python.org/
Source0:        %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz
Source1:        %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
Source2:        %{url}static/files/pubkeys.txt

%global         theme_version 2020.1
Source3:        %{pypi_source python-docs-theme %{theme_version}}

BuildArch:      noarch

Recommends:     python3 = %{version}
%{?python_provide:%python_provide %{name}}

BuildRequires:  %{__python3}
BuildRequires:  (python3-sphinx < 1:3 or python3-sphinx >= 1:3.2)
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  gnupg2

%bcond_without linkchecker
%if %{with linkchecker}
BuildRequires:  linkchecker
%endif


%description
The python3-docs package contains documentation on the Python 3
programming language and interpreter.

%prep
%gpgverify -k2 -s1 -d0
%autosetup -p1 -n Python-%{upstream_version}

# unpack the Sphinx theme to the right location
tar -xf %{SOURCE3} python-docs-theme-%{theme_version}/python_docs_theme
mv python-docs-theme-%{theme_version}/python_docs_theme Doc/tools
rmdir python-docs-theme-%{theme_version}

%build
make -C Doc html PYTHON=%{__python3}
rm Doc/build/html/.buildinfo

%install
mkdir -p %{buildroot}

%check
# Verify that all of the local links work (see rhbz#670493 - doesn't apply
# to python3-docs, but only to older python-docs)
#
# (we can't check network links, as we shouldn't be making network connections
# within a build.  Also, don't bother checking the .txt source files; some
# contain example URLs, which don't work)
%if %{with linkchecker}
linkchecker \
  --ignore-url=^mailto: --ignore-url=^http --ignore-url=^ftp \
  --ignore-url=.txt\$ --no-warnings \
  Doc/build/html/index.html
%endif

%files
%doc Misc/NEWS Misc/HISTORY Misc/README Doc/build/html

%changelog
* Tue Oct 06 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-1
- Update to 3.9.0 final

* Thu Sep 17 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0~rc2-1
- Update to 3.9.0rc2

* Thu Aug 13 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0~rc1-1
- Update to 3.9.0rc1

* Tue Jul 21 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0~b5-1
- Update to 3.9.0b5

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.0~b1-1
- Update to 3.9.0b1

* Wed Mar 25 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Fri Oct 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.0~rc1-1
- Update to 3.8.0rc1

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.0~b4-1
- Update to 3.8.0b4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Thu Apr 25 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Thu Dec 06 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-1
- Update to 3.7.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-0.1.rc1
- Update to 3.7.0rc1

* Thu Apr 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.5-2
- Only recommend the python3 package

* Thu Apr 05 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.6.5-1
- Update to 3.6.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.6.4-1
- Update to version 3.6.4

* Mon Oct 09 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.6.3-1
- Update to version 3.6.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.6.2-1
- Update to version 3.6.2

* Wed Mar 22 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.1-1
- Update to version 3.6.1 final

* Fri Mar 17 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.1-0.1.rc1
- Update to 3.6.1 release candidate 1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.6.0-1
- Update to current version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-2
- Rebuild for Python 3.6

* Mon Aug 22 2016 Tomas Orsava <torsava@redhat.com> - 3.5.2-1
- Update to current version
- Removed use-classic-theme.patch as it was no longer necessary

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Robert Kuska <rkuska@redhat.com> - 3.5.1-1
- Update to current version

* Mon Nov 16 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5.0-1
- Update to current version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Matej Stuchlik <mstuchli@redhat.com> - 3.4.3-1
- Rebuild for Python 3.4.3

* Tue Nov 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 3.4.2-1
- Rebuilt for Python 3.4.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.4.1-1
- Rebuilt for Python 3.4.1

* Mon Sep 16 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 3.3.2-2
- Patch docs build to use locally installed python3-sphinx.

* Wed Sep 04 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 3.3.2-1
- Initial package, spec adapted from python-docs.
