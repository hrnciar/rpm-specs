# vim: syntax=spec

Name: preproc-rpmspec
Version: 0.3
Release: 3%{?dist}
Summary: Minimalistic tool for rpm spec-file preprocessing
License: GPLv2+
URL: https://pagure.io/preproc-rpmspec.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/preproc-rpmspec.git#cd9594cd674ef58729779821feecb7812ae81e21:
%endif

# Source is created by:
# git clone https://pagure.io/preproc-rpmspec.git
# cd preproc-rpmspec
# git checkout preproc-rpmspec-0.3-1
# ./rpkg spec --sources
Source0: preproc-rpmspec-cd9594cd.tar.gz

BuildArch: noarch

Requires: bash
Requires: preproc
Requires: rpkg-macros

%description
Minimalistic tool to perform rpm spec-file preprocessing by using
preproc utilility and rpkg-macros. It can preprocess an rpm
spec file and print the result to stdout or to a file.

%prep
%setup -q -n preproc-rpmspec

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 preproc-rpmspec %{buildroot}%{_bindir}

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/preproc-rpmspec

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 clime <clime@fedoraproject.org> 0.3-2
- Rebuild

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.3-1
- no change, just a new tag

* Mon Mar 09 2020 clime <clime@fedoraproject.org> 0.2-1
- update description in spec

* Sun Mar 08 2020 clime <clime@fedoraproject.org> 0.1-1
- odd support for macros that produce files (git_archive/git_pack)
- replace --in-space with --output
- add note about the need to trust the spec files that are being preprocessed
- initial commit
