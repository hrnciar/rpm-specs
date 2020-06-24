# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/grpc/grpc-go
%global goipath         google.golang.org/grpc
%global forgeurl        https://github.com/grpc/grpc-go
Version:                1.24.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-grpc-grpc-go-devel < 1.18.0-3
}

%global goipaths0       google.golang.org/grpc
%global goipathsex0     google.golang.org/grpc/status google.golang.org/grpc/test google.golang.org/grpc/internal/transport google.golang.org/grpc/xds/internal/proto/envoy/api/v2

%if %{without bootstrap}
%global goipaths1       google.golang.org/grpc/status google.golang.org/grpc/test google.golang.org/grpc/internal/transport google.golang.org/grpc/xds/internal/proto/envoy/api/v2
%endif

%global common_description %{expand:
The Go language implementation of GRPC, http/2 based rpc.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTING.md README.md Documentation

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go language implementation of GRPC

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/golang/glog)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/hpack)
BuildRequires:  golang(golang.org/x/net/trace)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/oauth2/jwt)
BuildRequires:  golang(golang.org/x/sys/unix)
%if %{without bootstrap}
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/code)
%endif
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
# balancer/grpclb: needs network
%gocheck -d balancer/grpclb -d credentials/alts
%endif
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 02 2019 Kenneth Topp <toppk@bllue.org> - 1.24.0-1
- Release 1.24.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21.1-2
- Add Obsoletes for old name

* Tue Apr 23 15:38:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.21.1-1
- Release 1.21.1

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.0-2
- Unbootstrap

* Mon Feb 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.0-1
- Update to release v1.18.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5.git8e4536a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.10.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.10.0-2
- Upload glide files

* Wed May 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.10.0-1
- Update to v1.10.0
  resolves: #1423649

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-0.11.20180324gitbdb0727
- Bump to 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e

* Thu Mar 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.10.git5b3c4e8
- Bump to 5b3c4e850e90a4cf6a20ebd46c8b32a0a3afcb9e
  related: #1250461

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.9.20170407git8050b9c
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.git8050b9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.7.git8050b9c
- Bump to upstream 8050b9cbc271307e5a716a9d782803d09b0d6f2d
  related: #1250461

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.git777daa1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.git777daa1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.4.git777daa1
- Bump to upstream 777daa17ff9b5daef1cfdf915088a2ada3332bf0
  related: #1250461

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.git231b4cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.2.git231b4cf
- Polish the spec file
  related: #1250461

* Thu Sep 15 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.1.git231b4cf
- Bump to upstream 231b4cfea0e79843053a33f5fe90bd4d84b23cd3
  related: #1250461

* Mon Aug 08 2016 jchaloup <jchaloup@redhat.com> - 0-0.11.git02fca89
- Give back example provides, they are actually used by golang-github-cockroachdb-cmux-unit-test-devel
  related: #1250461

* Wed Aug 03 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.git02fca89
- Bump to upstream 02fca896ff5f50c6bbbee0860345a49344b37a03
  related: #1250461

* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.gite78224b
- Bump to upstream e78224b060cf3215247b7be455f80ea22e469b66
  related: #1250461

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitb062a3c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.gitb062a3c
- Bump to upstream b062a3c003c22bfef58fa99d689e6a892b408f9d
  related: #1250461

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.gitb88c12e
- Bump to upstream b88c12e7caf74af3928de99a864aaa9916fa5aad
  related: #1250461

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gite29d659
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 18 2016 jchaloup <jchaloup@redhat.com> - 0-0.4.gite29d659
- Bump to upstream e29d659177655e589850ba7d3d83f7ce12ef23dd
  related: #1250461

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd286668
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitd286668
- Update to spec-2.1
  resolves: #1250461

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd286668
- First package for Fedora
  resolves: #1246205