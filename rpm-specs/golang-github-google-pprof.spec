# Generated by go2rpm
%bcond_without check

# https://github.com/google/pprof
%global goipath         github.com/google/pprof
%global commit          f8f10df8421355d11843c3719debc9dec2cc1ad7

%gometa

%global common_description %{expand:
Pprof is a tool for visualization and analysis of profiling data.

Pprof reads a collection of profiling samples in profile.proto format and
generates reports to visualize and help analyze the data. It can generate both
text and graphical reports (through the use of the dot visualization package).}

%global golicenses      LICENSE LICENSE-*
%global godocs          doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Tool for visualization and analysis of profiling data

# Upstream license specification: BSD-3-Clause and Apache-2.0
# ASL 2.0: main package third_party/d3flamegraph
# BSD: third_party/d3 third_party/svgpan
License:        BSD and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/ianlancetaylor/demangle)

%description
%{common_description}

%gopkg

%prep
%goprep
mv third_party/d3/LICENSE LICENSE-d3
mv third_party/d3flamegraph/LICENSE LICENSE-d3flamegraph
mv third_party/svgpan/LICENSE LICENSE-svgpan

%build
%gobuild -o %{gobuilddir}/bin/pprof %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 10:33:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190623gitf8f10df
- Bump to commit f8f10df8421355d11843c3719debc9dec2cc1ad7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git2b5d435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git2b5d435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git2b5d435
- Bump to commit 2b5d4350d687b058368c98ab141d34d08162ec7b

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git6167805
- First package for Fedora
