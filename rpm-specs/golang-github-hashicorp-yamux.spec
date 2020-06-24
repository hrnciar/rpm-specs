# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/hashicorp/yamux
%global goipath         github.com/hashicorp/yamux
%global commit          2f1d1f20f75d5404f53b9edf6b53ed5505508675

%gometa

%global common_description %{expand:
Yamux (Yet another Multiplexer) is a multiplexing library for Golang. It relies
on an underlying connection to provide reliability and ordering, such as TCP or
Unix domain sockets, and provides stream-oriented multiplexing. It is inspired
by SPDY but is not interoperable with it.}

%global golicenses      LICENSE
%global godocs          README.md spec.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.19%{?dist}
Summary:        Golang connection multiplexing library

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

# Remove in F33
# Remove erroneous glide.lock folder
%pretrans devel -p <lua>
path = "%{gopath}/src/%{goipath}/glide.lock"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path)
end

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 20:44:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20190430git2f1d1f2
- Bump to commit 2f1d1f20f75d5404f53b9edf6b53ed5505508675

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.gitdf94978
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitdf94978
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20151129gitdf94978
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitdf94978
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitdf94978
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitdf94978
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitdf94978
- Bump to upstream df949784da9ed028ee76df44652e42d37a09d7e4
  related: #1250478

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitb2e5585
- Update to spec-2.1
  related: #1250478

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitb2e5585
- Update spec file to spec-2.0
- Disable check due to failing test
  resolves: #1250478

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitb2e5585
- First package for Fedora
  resolves: #1212111