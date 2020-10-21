# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/apiserver
%global goipath         k8s.io/apiserver
%global forgeurl        https://github.com/kubernetes/apiserver
Version:                1.18.9
%global tag             kubernetes-1.18.9
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
This library contains code to create Kubernetes aggregation server complete with
delegated authentication and authorization, kubectl compatible discovery
information, optional admission chain, and versioned types. It's first consumers
are k8s.io/kubernetes, k8s.io/kube-aggregator, and
github.com/kubernetes-incubator/service-catalog.}

%global golicenses      LICENSE
%global godocs          code-of-conduct.md CONTRIBUTING.md README.md

%global gosupfiles      ${example[@]}

Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for writing a Kubernetes-style API server

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-Use-klog-v2.patch
# Backport for sigs.k8s.io/apiserver-network-proxy
Patch1:         https://github.com/kubernetes/apiserver/commit/c78dd46c272b441707c6c0d5222802eba8d4edba.patch#/0001-fix-API-change-in-apiserver-network-proxy.patch

BuildRequires:  golang(bitbucket.org/ww/goautoneg)
BuildRequires:  golang(github.com/coreos/go-oidc)
BuildRequires:  golang(github.com/coreos/go-systemd/daemon)
BuildRequires:  golang(github.com/docker/docker/pkg/term)
BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gnostic-0.4/compiler)
BuildRequires:  golang(github.com/googleapis/gnostic-0.4/openapiv2)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/hashicorp/golang-lru)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go.etcd.io/etcd/client)
BuildRequires:  golang(go.etcd.io/etcd/clientv3)
BuildRequires:  golang(go.etcd.io/etcd/etcdserver)
BuildRequires:  golang(go.etcd.io/etcd/etcdserver/api/etcdhttp)
BuildRequires:  golang(go.etcd.io/etcd/etcdserver/api/v2http)
BuildRequires:  golang(go.etcd.io/etcd/etcdserver/api/v3rpc/rpctypes)
BuildRequires:  golang(go.etcd.io/etcd/integration)
BuildRequires:  golang(go.etcd.io/etcd/mvcc/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/pkg/testutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/transport)
BuildRequires:  golang(go.etcd.io/etcd/pkg/types)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/api/admission/v1)
BuildRequires:  golang(k8s.io/api/admission/v1beta1)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1)
BuildRequires:  golang(k8s.io/api/auditregistration/v1alpha1)
BuildRequires:  golang(k8s.io/api/authentication/v1)
BuildRequires:  golang(k8s.io/api/authentication/v1beta1)
BuildRequires:  golang(k8s.io/api/authorization/v1)
BuildRequires:  golang(k8s.io/api/authorization/v1beta1)
BuildRequires:  golang(k8s.io/api/coordination/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/flowcontrol/v1alpha1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation/path)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/cache)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/clock)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/mergepatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/rand)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/uuid)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/waitgroup)
BuildRequires:  golang(k8s.io/apimachinery/pkg/version)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/informers)
BuildRequires:  golang(k8s.io/client-go/informers/auditregistration/v1alpha1)
BuildRequires:  golang(k8s.io/client-go/informers/core/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/authentication/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/authorization/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/flowcontrol/v1alpha1)
BuildRequires:  golang(k8s.io/client-go/listers/admissionregistration/v1)
BuildRequires:  golang(k8s.io/client-go/listers/core/v1)
BuildRequires:  golang(k8s.io/client-go/listers/flowcontrol/v1alpha1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(k8s.io/client-go/tools/events)
BuildRequires:  golang(k8s.io/client-go/tools/record)
BuildRequires:  golang(k8s.io/client-go/util/cert)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/keyutil)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)
BuildRequires:  golang(k8s.io/component-base/cli/flag)
BuildRequires:  golang(k8s.io/component-base/featuregate)
BuildRequires:  golang(k8s.io/component-base/logs)
BuildRequires:  golang(k8s.io/component-base/metrics)
BuildRequires:  golang(k8s.io/component-base/metrics/legacyregistry)
BuildRequires:  golang(k8s.io/component-base/metrics/testutil)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/builder)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/common)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/handler)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/schemaconv)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  golang(k8s.io/utils/net)
BuildRequires:  golang(k8s.io/utils/path)
BuildRequires:  golang(k8s.io/utils/trace)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/fieldpath)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/merge)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/typed)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/value)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/coreos/pkg/capnslog)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/square/go-jose.v2)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/batch/v1)
BuildRequires:  golang(k8s.io/api/extensions/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/testapigroup/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/selection)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api/v1)
BuildRequires:  golang(k8s.io/component-base/featuregate/testing)
BuildRequires:  golang(k8s.io/utils/pointer)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1
sed -i "s|github.com/munnerz/goautoneg|bitbucket.org/ww/goautoneg|" $(find . -name "*.go")
sed -i "s|github.com/googleapis/gnostic/OpenAPIv2|github.com/googleapis/gnostic/openapiv2|" $(find . -name "*.go")
sed -i "s|k8s.io/klog|k8s.io/klog/v2|" $(find . -name "*.go")
sed -i 's|github.com/googleapis/gnostic|github.com/googleapis/gnostic-0.4|' $(find . -iname "*.go" -type f)
sed -i 's|sigs.k8s.io/structured-merge-diff/v3|sigs.k8s.io/structured-merge-diff/v4|' $(find . -iname "*.go" -type f)

%install
mapfile -t example <<< $(find pkg/apis/example* -type f)
%gopkginstall

%if %{with check}
%check
# pkg/admission/configuration, pkg/admission/plugin/webhook, pkg/audit, pkg/authorization/authorizerfactory, pkg/registry/generic/registry → pkg/server/egressselector/
%gocheck -d pkg/storage/value/encrypt/envelope \
         -t pkg/endpoints \
         -d pkg/apis/config/validation \
         -d pkg/admission/configuration \
         -t pkg/admission/plugin/webhook \
         -t pkg/audit \
         -d pkg/authorization/authorizerfactory \
         -d pkg/registry/generic/registry \
         -t pkg/server \
         -d pkg/storage/storagebackend/factory \
         -d pkg/util/webhook \
         -t plugin/pkg
%endif

%gopkgfiles

%changelog
* Tue Sep 29 19:06:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Wed Aug 19 00:22:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-6
- Update import pash for sigs.k8s.io/structured-merge-diff/v3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-3
- Backport for sigs.k8s.io/apiserver-network-proxy

* Mon Jun 15 21:22:46 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-2
- Reinclude sigs.k8s.io/apiserver-network-proxy

* Mon Jun 15 17:37:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Sun Apr 12 23:26:50 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Feb 05 22:25:59 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 17:12:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 13 01:09:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package
