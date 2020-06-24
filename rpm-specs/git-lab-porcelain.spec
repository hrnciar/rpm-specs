%global fullcommit 75a12220b55d8ae4df68189b9ee0358f953223c9
%global shortcommit %(fcstr=%{fullcommit} && echo ${fcstr:0:8})
# %%global date        %%(date +%%Y%%m%%d) # hardcode so it matches a changelog
%global date        2020325
%global execname    git-lab

Name:      git-lab-porcelain
Version:   0
Release:   %{date}git%{shortcommit}%{?dist}.1
Summary:   Git porcelain for working with git-lab

License:   GPLv3
URL:       https://gitlab.com/nhorman/%{name}
Source0:   %{url}/-/archive/%{fullcommit}/%{name}-%{fullcommit}.tar.gz
BuildArch: noarch

Requires: python3-gitlab
Requires: python3-GitPython
Requires: python3-pycurl
Requires: python3-tabulate
Requires: curl

%description
A porcelain for git to facilitate command line creation/listing/editing
and reviewing of merge requests in git-lab.

%prep
%autosetup -n git-lab-porcelain-%{fullcommit}

%build
# nothing to do here

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -p -m 0755 %{execname} %{buildroot}/%{_bindir}/%{execname}
install -p -m 0644 man1/* %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/%{execname}
%{_mandir}/man1/*
%license LICENSE

%changelog
* Wed Mar 25 2020 Neil Horman <nhorman@redhat.com>
- Update to latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20200123git4eeaa725.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Vladis Dronov <vdronoff+fedora@gmail.com> - 0-20200123git4eeaa725
- Update sources to the latest upstream

* Tue Jan 21 2020 Vladis Dronov <vdronoff+fedora@gmail.com> - 0-20200121git9f421f38
- Initial release for the Fedora 29-31 and Rawhide
