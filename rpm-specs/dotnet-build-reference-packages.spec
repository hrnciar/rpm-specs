%global debug_package %{nil}

%global commit 5aaf20dca19adfd99433bb962306d859cf014d1b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dotnet-build-reference-packages
Version:        0
Release:        4.20200608git%{shortcommit}%{?dist}
Summary:        Reference packages needed by the .NET Core SDK build

License:        MIT
URL:            https://github.com/dotnet/source-build-reference-packages
Source0:        https://github.com/dotnet/source-build-reference-packages/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  dotnet-sdk-3.1
BuildRequires:  dotnet-sdk-3.1-source-built-artifacts

%description
This contains references packages used for building .NET Core.

This is not meant to be used by end-users.


%prep
%setup -q -n source-build-reference-packages-%{commit}

find -name '*.nupkg' -type f -delete
find -name '*.dll' -type f -delete
find -name '*.so' -type f -delete
find -name '*.tar.gz' -type f -delete

%build
find -iname 'nuget.config' -exec echo {} \; -exec cat {} \;

%{_libdir}/dotnet/dotnet --info

./build.sh \
  --with-sdk %{_libdir}/dotnet \
  --with-packages %{_libdir}/dotnet/source-built-artifacts/*.tar.gz

pushd artifacts/reference-packages
tar cvzf Private.SourceBuild.ReferencePackages.%{version}.tar.gz *.nupkg
popd
mv artifacts/reference-packages/Private.SourceBuild.ReferencePackages.%{version}.tar.gz .

%install
mkdir -p %{buildroot}/%{_libdir}/dotnet
cp -a artifacts/reference-packages %{buildroot}/%{_libdir}/dotnet/
cp -a Private.SourceBuild.ReferencePackages.%{version}.tar.gz %{buildroot}/%{_libdir}/dotnet/reference-packages/


%files
%dir %{_libdir}/dotnet/
%{_libdir}/dotnet/reference-packages/
%license LICENSE.txt


%changelog
* Fri Jun 19 2020 Omair Majid <omajid@redhat.com> - 0-4.20200608git5aaf20d
- Enable building on aarch64

* Mon Jun 08 2020 Chris Rummel <crummel@microsoft.com> - 0-3.20200608git5aaf20d
- Updated to upstream commit 5aaf20d

* Tue Jun 02 2020 Omair Majid <omajid@redhat.com> - 0-3.20200528git6e2aee66e2aee6
- Updated to upstream commit 6e2aee6

* Wed Feb 19 2020 Radka Janekova <rjanekov@redhat.com> - 0-2.20200108git9cc7dad
- Added license reference
* Tue Feb 11 2020 Omair Majid <omajid@redhat.com> - 0-1.20200108git9cc7dad
- Initial package