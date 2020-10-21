%bcond_without check

%global _hardened_build 1

%global distprefix %{nil}

# https://github.com/aliyun/aliyun-cli
%global goipath0        github.com/aliyun/aliyun-cli
Version:                3.0.60

# https://github.com/aliyun/aliyun-openapi-meta
%global goipath1        github.com/aliyun/aliyun-openapi-meta
%global version1        0
%global commit1         af98eafaf38bb8dca2d0b205de88e9b1e7e7bb29

%gometa -a

%global _docdir_fmt     %{name}

%global godevelsummary0 Alibaba Cloud (Aliyun) CLI
%global godevelsummary1 Alibaba Cloud (Aliyun) OpenAPI Meta Data

%global common_description %{expand:
Alibaba Cloud (Aliyun) CLI.}

%global golicenses0     LICENSE
%global godocs0         CHANGELOG.md README-CN.md README.md README-bin.md\\\
                        README-cli.md README-CN-oss.md README-oss.md

%global golicenses1     LICENSE
%global godocs1         README-openapi-meta.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        %{godevelsummary0}

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource0}
Source1:        %{gosource1}

# https://github.com/aliyun/aliyun-cli/pull/300
Patch0:         aliyun-cli-credentials-config.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1866529
# https://github.com/aliyun/aliyun-cli/issues/303
ExcludeArch:    armv7hl                   # (#1866529)

BuildRequires:  golang-github-shulhan-bindata
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/endpoints)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/ecs)
BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/aliyun/credentials-go/credentials)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/jmespath/go-jmespath)
BuildRequires:  golang(github.com/posener/complete)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  help2man

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  zsh
%endif

%description
%{common_description}

%gopkg

%prep
%goprep -a
cd %{gosourcedir}
%patch0 -p1
mv bin/README.md README-bin.md
mv cli/README.md README-cli.md
mv oss/README.md README-oss.md
mv oss/README-CN.md README-CN-oss.md
mv %{_builddir}/%{extractdir1}/README.md %{_builddir}/%{extractdir1}/README-openapi-meta.md
rm %{gobuilddir}/src/%{goipath0} %{gobuilddir}/src/%{goipath1}
ln -fs %{_builddir}/%{extractdir1} %{_builddir}/aliyun-openapi-meta
go-bindata.shulhan -o resource/metas.go -pkg resource ../aliyun-openapi-meta/...
rm %{_builddir}/aliyun-openapi-meta
ln -fs %{_builddir}/%{extractdir0} %{gobuilddir}/src/%{goipath0}
ln -fs %{_builddir}/%{extractdir1} %{gobuilddir}/src/%{goipath1}

%build
LDFLAGS="-X '%{goipath0}/cli.Version=%{version}'" 
%gobuild -o %{gobuilddir}/bin/aliyun %{goipath0}/main
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{godevelsummary0}" -s 1 -o %{gobuilddir}/share/man/man1/aliyun.1 -N --version-string="%{version}" %{gobuilddir}/bin/aliyun

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
cp -Trv /etc/skel %{getenv:HOME}
# Skip 'openapi' and 'oss/lib' tests due to need for credentials
%gocheck -d 'openapi' -d 'oss/lib'
%endif

%files
%license ../%{extractdir0}/LICENSE
%doc ../%{extractdir0}/CHANGELOG.md
%doc ../%{extractdir0}/README-CN.md     ../%{extractdir0}/README.md
%doc ../%{extractdir0}/README-bin.md    ../%{extractdir0}/README-cli.md
%doc ../%{extractdir0}/README-CN-oss.md ../%{extractdir0}/README-oss.md
%doc ../%{extractdir1}/README-openapi-meta.md
%{_mandir}/man1/aliyun.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Oct 13 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.60-1
- Update to version 3.0.60 (#1887004)
- Update to aliyun-openapi-meta to commit
  af98eafaf38bb8dca2d0b205de88e9b1e7e7bb29

* Mon Sep 21 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.59-1
- Update to version 3.0.59 (#1880672)
- Update to aliyun-openapi-meta to commit
  944de0a2cc8e892728004bfa63a2d2964a49469b

* Wed Sep 16 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.58-1
- Update to version 3.0.58 (#1879465)
- Update to aliyun-openapi-meta to commit
  67c5e4302ba6c8207e4176e57145df677af30976

* Thu Aug 06 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.56-1
- Update to version 3.0.56 (#1866826)
- Update to aliyun-openapi-meta to commit
  e7acae2e91780bc24a4b71c17803dec5dbb0989f
- Copy skeleton dot files to HOME directory for TestCompletionInstallers

* Wed Aug 05 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-6
- ExcludeArch armv7hl due to build failing from running out of memory (#1866529)
- Explicitly include zsh BuildRequires for tests on s390x

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-5
- Use go-bindata.shulhan instead of go-bindata
  https://github.com/aliyun/aliyun-cli/issues/262

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-4
- Set distprefix to nil
- Clean up unneeded globals
- Rename openapi-meta README.md for proper inclusion
- Requre new go-bindata
- Use standard goprep
- Prevent symbolic link infinite loops
- New aliyun-openapi-meta paths
- Added paths to license and doc in main package

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-3
- Update summary and description for clarity and consistency

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-2
- Reenable check stage
- Disable 'openapi' tests due to only being used by meta
- Disable 'oss/lib' tests due to need for credentials

* Sat Aug 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-1
- Update to version 3.0.55 (#1811183)
- Disable check stage temporarily
- Update to aliyun-openapi-meta to commit
  fb1de10319cf130af8945963ef6659707b5f04b7
- Add godevelsummary, golicenses, and godocs for all sources
- Reorder goprep and patch operations
- Remove goenv before gobuild
- Explicitly set man page summary
- Use standard gopkginstall and gopkgfiles
- Properly generate debugsourcefiles.list

* Fri Jul 31 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-3
- Patch to build against golang-github-aliyun-credentials-1.1.0

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-2
- Enable check stage
- Rename godocs in subdirectories
- Remove explicit gzip of man page
- Change gometaabs from define to global

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-1
- Update to version 3.0.54 (#1811183)
- Explicitly harden package
- Update to aliyun-openapi-meta to commit
  73a3ade39a109bda00ae3a80585fac98b3f3dd70
- Remove golang(github.com/satori/go.uuid)
  (commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b) BuildRequires
- Fix man page generation
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-2
- Add man page

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-1
- Update to aliyun-cli to version 3.0.36
- Update to aliyun-openapi-meta to commit
  3e9d6a741c5029c92f6447e4137a6531f037a931

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 3.0.30-1
- Initial package

