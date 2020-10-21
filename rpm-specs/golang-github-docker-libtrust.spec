# Generated by go2rpm
%bcond_without check

# https://github.com/docker/libtrust
%global goipath         github.com/docker/libtrust
%global commit          aabc10ec26b754e797f9028f4589c5b7bd90dc20

%gometa

%global common_description %{expand:
Libtrust is library for managing authentication and authorization using public
key cryptography.

Authentication is handled using the identity attached to the public key.
Libtrust provides multiple methods to prove possession of the private key
associated with an identity:

 - TLS x509 certificates
 - Signature verification
 - Key Challenge

Authorization and access control is managed through a distributed trust graph.
Trust servers are used as the authorities of the trust graph and allow caching
portions of the graph for faster access.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md tlsdemo/README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.22%{?dist}
Summary:        Primitives for identity and authorization

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 23:22:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.19.20190501gitaabc10e
- Bump to commit aabc10ec26b754e797f9028f4589c5b7bd90dc20

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.17.gitfa56704
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gitfa56704
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20150114gitfa56704
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfa56704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitfa56704
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sat Mar 05 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.gitfa56704
- Bump to upstream fa567046d9b14f6aa788882a950d69651d230b21
  related: #1248803

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git6b78349
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git6b78349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git6b78349
- Update to spec-2.1
  related: #1248803

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git6b78349
- Update spec file to spec-2.0
  resolves: #1248803

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git6b78349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.git6b78349
- update to latest upstream master

* Fri Oct 17 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.gitd273ef2
- Resolves: rhbz#1154165 - initial package

