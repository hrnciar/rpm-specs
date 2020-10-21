# Review https://bugzilla.redhat.com/show_bug.cgi?id=1249329
%global commit0 b567f41830f3ac814e71688f9d2e13ea337f618d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:          percol
Version:       0.1.1
Release:       0.19%{?shortcommit0:.git.%{shortcommit0}}%{?dist}
Summary:       Interactive selection to the traditional pipe concept on UNIX

License:       MIT
URL:           https://github.com/mooz/percol
%if 0%{?commit0:1}
Source0:       https://github.com/mooz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:       https://github.com/mooz/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-cmigemo
# BuildRequires to run test
BuildRequires: python3-six python3-cmigemo
Requires:      python3-six python3-cmigemo

%description
percol is an interactive grep tool in your terminal. percol

receives input lines from stdin or a file,
lists up the input lines,
waits for your input that filter/select the line(s),
and finally outputs the selected line(s) to stdout.
Since percol just filters the input and output the result to stdout, it can be
used in command-chains with | in your shell (UNIX philosophy!).

%prep
%if 0%{?commit0:1}
%setup -qn %{name}-%{commit0}
%else
%setup -q
%endif

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} setup.py test

%files
%{_bindir}/%{name}
%doc README.md
%{python3_sitelib}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.19.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-0.18.git.b567f41
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.17.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-0.16.git.b567f41
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-0.15.git.b567f41
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.14.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.13.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.12.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-0.11.git.b567f41
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.10.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.9.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.8.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-0.7.git.b567f41
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-0.6.git.b567f41
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.5.git.b567f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.1-0.4.git.b567f41
- Add BuildRequires: python3-six python3-cmigemo for test run.

* Sun Nov 29 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.1-0.3.git.b567f41
- Review done.
- Use new python pacroses %%py3_build and %%py3_install.

* Sat Nov 28 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.1-0.2.git.b567f41
- Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=1249329. Thanks to Julien Enselme.
- Change License to MIT (GPL statements removed: https://github.com/mooz/percol/commit/d0bc902555fff5abef85012af3cbc323b915843b).
- Requested license text inclusion: https://github.com/mooz/percol/issues/87
- Add requires python3-cmigemo

* Sun Jul 26 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.1-0.1.git.b567f41
- Master build, two problems reported by me addressed now:
    o FSF address: https://github.com/mooz/percol/issues/77
    o Python3 compatability - https://github.com/mooz/percol/issues/78

* Sun Jul 26 2015 Pavel Alexeev (aka Pahan-Hubbitus) <Pahan@Hubbitus.info> - 0.1.0-1
- Initial version
- Incorrect fsf address reported: https://github.com/mooz/percol/issues/77