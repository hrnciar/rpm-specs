%global sum()   A simple %* wrapper around inotify
%global desc \
inotify_simple is a simple Python wrapper around inotify. No fancy bells and \
whistles, just a literal wrapper with ctypes. Only 122 lines of code!

%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%global sname inotify_simple

Name:           python-%sname
Version:        1.3.4
Release:        1%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        BSD
URL:            https://github.com/chrisjbillington/%sname
Source0:        https://pypi.org/packages/source/i/%sname/%sname-%version.tar.gz

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-enum34
BuildRequires: python2-setuptools
%endif
%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif


%description
%desc


%if %{with python2}
%package -n     python2-%sname
Summary:        %{sum Python 2}
Requires:       python2-enum34

%description -n python2-%sname
%{desc}
%endif


%if %{with python3}
%package -n     python3-%sname
Summary:        %{sum Python 3}

%description -n python3-%sname
%{desc}
%endif


%prep
%autosetup -n %sname-%version -p1


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%if %{with python2}
%files -n python2-%sname
%license LICENSE
%python2_sitelib/%sname.py*
%python2_sitelib/%sname-%{version}*.egg-info
%endif


%if %{with python3}
%files -n python3-%sname
%license LICENSE
%python3_sitelib/%sname.py
%python3_sitelib/%sname-%{version}*.egg-info
%python3_sitelib/__pycache__/inotify_simple*
%endif


%changelog
* Tue Aug 04 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.4-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.3-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.2
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3.1-1
- new upstream release, per release notes:
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.3.1
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.2.1
  https://github.com/chrisjbillington/inotify_simple/releases/tag/1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-2
- Drop Python 2 package on Fedora > 29 (#1627432)

* Fri Aug 17 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1.8-1
- initial RPM packaging
